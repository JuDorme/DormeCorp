
from connectors.kraken_connector import KrakenConnector

k = KrakenConnector()
#print(k.get_balance())
#print(k.get_market_depth())
print(k.get_open_orders())