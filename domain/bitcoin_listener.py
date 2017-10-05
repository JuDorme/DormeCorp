import threading
from domain.bitcoin_service import get_bitcoin_ref_price
from domain.bitcoin_service import get_bitcoin_euro
from domain.bitcoin_service import set_bitcoin_ref_price
from domain.mail_service import send_email

def printit():
  threading.Timer(5.0, printit).start()
  ref_price = float(get_bitcoin_ref_price())
  current_price = float(get_bitcoin_euro())
  threashold = 0.0003

  if current_price != -1:
      if current_price > (1+ threashold)*ref_price or current_price < (1- threashold)*ref_price:

          set_bitcoin_ref_price(current_price)
          print('Mail sent')
          print('New ref price : ' + str(get_bitcoin_ref_price()))
      else:
        move = 'move : ' + str(round((current_price/ref_price-1)*100,2)) + ' current price : ' + str(current_price) + ' ref price : ' + str(ref_price)
        print(move)
  else:
      print('connection lost !')
printit()