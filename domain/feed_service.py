def get_bitcoin_euro():
    request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return request.json()