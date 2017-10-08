from connectors.PyRock import PyRock

class RockConnector():

    def __init__(self):
        with open('..\\..\\rocktrading.key', 'r') as f:
            self.key = f.readline().strip()
            self.secret = f.readline().strip()
        self.r = PyRock(self.key,self.secret)

    def get_balance(self):
        return self.r.AllBalances()

    def get_market_depth(self, depth=1):
        res = self.r.OrderBook('BTCEUR')
        res['asks'] = res['asks'][:depth]
        res['bids'] = res['bids'][:depth]
        return res

