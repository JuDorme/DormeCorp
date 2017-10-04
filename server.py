from flask import Flask
from domain.bitcoin_service import get_bitcoin_euro
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DormeCorp!"

@app.route("/price")
def bitcoin_euro():
    return get_bitcoin_euro()