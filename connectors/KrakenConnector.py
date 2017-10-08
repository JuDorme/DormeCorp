import krakenex
from enum import Enum

class KrakenConnector():


    def __init__(self):
        self.k = krakenex.API()
        self.k.load_key('..\\..\\kraken.key')

    def get_balance(self):
        return self.k.query_private('Balance')

    def get_market_depth(self, depth=1):

        res = self.k.query_public('Depth', {'pair': 'XXBTZEUR', 'count': str(depth)})
        if res['error'] == []:
            return res['result']['XXBTZEUR']
        else:
            return res['error']

    def place_conditionnal_order(self, way, ordertype,price,volume):
        return self.k.query_private('AddOrder',
                        {'pair': 'XXBTZEUR',
                         'type': way,
                         'ordertype': ordertype,
                         'price': price,
                         'volume': volume,
                         })
    def get_open_orders(self):
        return self.k.query_private('OpenOrders')

    def get_open_positions(self):
        # prepare request
        req_data = {'docalcs': 'true'}

        # querry servers
        start = self.k.query_public('Time')
        open_positions = self.k.query_private('OpenPositions', req_data)
        end = self.k.query_public('Time')
        latency = end['result']['unixtime'] - start['result']['unixtime']
        return  open_positions

    def cancel_order(self, txid):
        txid_data = {'txid' : txid}
        return self.k.query_private('CancelOrder',txid_data)

class KrakenOrderType(Enum):
    LIMIT = 'orderlimit'
