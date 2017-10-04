import requests

def get_bitcoin_euro():
    request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    rjson = request.json()
    res = str(rjson['bpi']['EUR']['rate'])
    return res