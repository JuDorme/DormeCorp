from enum import Enum
class Order():

    def __init__(self):
        self.way = OrderWay.UNKNOWN
        self.price = 0
        self.quantity = 0
        self.origin = OrderOrigin.UNKNOWN

class OrderWay(Enum):
    BID = 'bid'
    ASK = 'ask'
    UNKNOWN = 'unknown'

class OrderOrigin(Enum):
    KRAKEN = 'kraken'
    ROCK = 'rock'
    UNKNOWN = 'unknown'