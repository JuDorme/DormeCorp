
from connectors.KrakenConnector import KrakenConnector
from connectors.RockConnector import RockConnector
k = KrakenConnector()
r = RockConnector()


rock_market = r.get_market_depth()
kraken_market = k.get_market_depth()

if 'bids' in kraken_market:
    kraken_bid = float(kraken_market['bids'][0][0])
    kraken_ask = float(kraken_market['asks'][0][0])
else:
    print(kraken_market)

if 'bids' in rock_market:
    rock_bid = float(rock_market['bids'][0]['price'])
    rock_ask = float(rock_market['asks'][0]['price'])
else:
    print(rock_market)

#i can sell max_bid :
min_bid = min(kraken_bid,rock_bid)
max_bid = max(kraken_bid,rock_bid)
#i can buy min ask :
min_ask = min(kraken_ask,rock_ask)
max_ask = max(kraken_ask,rock_ask)


print('I can buy at ' + str(min_ask) + ' and sell at ' + str(max_bid))