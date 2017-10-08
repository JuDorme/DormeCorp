from connectors.KrakenConnector import KrakenConnector
from connectors.RockConnector import RockConnector
from domain.Order import Order
from domain.Order import OrderWay
from domain.Order  import OrderOrigin
import threading

import logging
from logging.handlers import RotatingFileHandler
# logger settings
log = logging.getLogger()
log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
file_handler = RotatingFileHandler('arbitrage.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
log.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
log.addHandler(stream_handler)



def arbitrage_detector():

    threading.Timer(20.0, arbitrage_detector).start()

    k = KrakenConnector()
    r = RockConnector()

    rock_market = r.get_market_depth()
    kraken_market = k.get_market_depth()

    if 'bids' in kraken_market:
        kraken_bid = get_kraken_bid(kraken_market)

        kraken_ask = get_kraken_ask(kraken_market)

    else:
        print(kraken_market)

    if 'bids' in rock_market:
        rock_bid = get_rock_bid(rock_market)
        rock_ask = get_rock_ask(rock_market)

    else:
        print(rock_market)

    #i can sell max_bid :
    best_bid = get_best_bid([kraken_bid,rock_bid])

    #i can buy min ask :
    best_ask = get_best_ask([kraken_ask,rock_ask])



    #quantity


    log.info('I can buy at ' + str(best_ask.price) + ' and sell at ' + str(best_bid.price) + ' profit brut ' + str(round((best_bid.price/best_ask.price-1)*100,2)) + '%' + ' qte buy/sell ' + str(best_ask.quantity) + ' / ' + str(best_bid.quantity) + ' buy ' + best_ask.origin.value + ' sell ' + best_bid.origin.value)
    return




def get_kraken_bid(kraken_market, depth = 0):
    res = Order()
    try:
        res.price = float(kraken_market['bids'][depth][0])
        res.way = OrderWay.BID
        res.quantity = float(kraken_market['bids'][depth][1])
        res.origin = OrderOrigin.KRAKEN
        return res
    except :
        log.info(kraken_market)
        return res

def get_kraken_ask(kraken_market, depth=0):
    res = Order()

    try:
        res.price = float(kraken_market['asks'][depth][0])
        res.way = OrderWay.ASK
        res.quantity = float(kraken_market['asks'][depth][1])
        res.origin = OrderOrigin.KRAKEN
        return res
    except:
        log.info(kraken_market)
        return res

def get_rock_bid(rock_market, depth = 0):
    res = Order()
    res.price = float(rock_market['bids'][depth]['price'])
    res.way = OrderWay.BID
    res.quantity = float(rock_market['bids'][depth]['amount'])
    res.origin = OrderOrigin.ROCK
    return res

def get_rock_ask(rock_market, depth = 0):
    res = Order()
    res.price = float(rock_market['asks'][depth]['price'])
    res.way = OrderWay.ASK
    res.quantity = float(rock_market['asks'][depth]['amount'])
    res.origin = OrderOrigin.ROCK
    return res

def get_best_bid(order_list):
    best_order = Order()
    for order in order_list:
        if  order.price > best_order.price:
            best_order = order

    return best_order

def get_best_ask(order_list):
    best_order = Order()
    best_order.price = 999999999 #The day this is fucked up, we will have enough money :)
    for order in order_list:
        if order.price < best_order.price:
            best_order = order
    return best_order

arbitrage_detector()