from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DormeCorp!"

def bitcoin_euro():
    return get_bitcoin_euro()