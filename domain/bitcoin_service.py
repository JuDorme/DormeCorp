import requests
import csv
import sys

def get_bitcoin_euro():
    res = -1
    try:
        request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        rjson = request.json()
        res = rjson['bpi']['EUR']['rate_float']

    except:
        print('Unexpected error:', sys.exc_info()[0])
        raise
    finally:
        return res

def get_bitcoin_ref_price():
        csvfile = open('C:\\Homeware\\DormeCorp\\database\\refprice.csv', 'rt' )
        try:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row:
                    continue
                else:
                    res = row[0]
        finally:
            csvfile.close()
        return res

def set_bitcoin_ref_price(new_price):
    csvfile = open('C:\\Homeware\\DormeCorp\\database\\refprice.csv', 'wt')
    try:
        writer = csv.writer(csvfile)
        row = []
        row.append(str(new_price))
        writer.writerow(row)
    finally:
        csvfile.close()