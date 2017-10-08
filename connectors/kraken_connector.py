import krakenex
from enum import Enum

class krakenConnector():

    def __init__(self):
        self.data = []
        k = krakenex.API()
        k.load_key('..\\..\\kraken.key')

    def get_balance(self):
        return self.k.query_private('Balance')

    def get_market_depth(self, depth=1):
        return self.k.query_public('Depth', {'pair': 'XXBTZEUR', 'count': str(depth)})

    def place_conditionnal_order(self, way, ordertype,price,volume):
        return self.k.query_private('AddOrder',
                        {'pair': 'XXBTZEUR',
                         'type': way,
                         'ordertype': ordertype,
                         'price': price,
                         'volume': volume,
                         })

    def get_open_positions(self):
        # prepare request
        req_data = {'docalcs': 'true'}

        # querry servers
        start = self.k.query_public('Time')
        open_positions = self.k.query_private('OpenPositions', req_data)
        end = self.k.query_public('Time')
        latency = end['result']['unixtime'] - start['result']['unixtime']

        # parse result
        dict(open_positions)

        b = 0
        c = 0
        for i in open_positions['result']:
            order = open_positions['result'][i]
            if (order['pair'] == 'XETHZEUR'):
                b += (float(order['vol']))
            if (order['pair'] == 'XXBTZEUR'):
                c += (float(order['vol']))
        return c

    def cancel_orders(self):
        #id necessary ? to check.
        return self.k.query_private('CancelOrder')

class krakenOrderType(Enum):
    LIMIT = 'orderlimit'