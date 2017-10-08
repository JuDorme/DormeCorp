from enum import Enum
class Order():

    def __init__(self):
        self.way = OrderWay.UNKNOWN
        self.price = 0
        self.quantity = 0

class OrderWay(Enum):
    BID = 'bid'
    ASK = 'ask'
    UNKNOWN = 'unknown'