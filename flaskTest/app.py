import random
import re
import sys
from flask import Flask, render_template
from turbo_flask import Turbo

import threading
import time

from bitmex import bitmex
import requests, json
from datetime import datetime


app = Flask(__name__)

turbo = Turbo(app)

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

def update_load():
    with app.app_context():
        while True:
            time.sleep(0.05)
            turbo.push(turbo.replace(render_template('loadavg.html'), 'load'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.context_processor
def inject_load():
    api_key = ''
    api_secret = ''
    client = bitmex(test=False, api_key=api_key, api_secret=api_secret)
    response = requests.get("https://www.bitmex.com/api/v1/orderBook/L2?symbol=eth&depth=1").json()

    eth_ask_price = response[0]['price']
    return {'load1': eth_ask_price,}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)

'''
@app.context_processor
def inject_load():
    if sys.platform.startswith('linux'): 
        with open('/proc/loadavg', 'rt') as f:
            load = f.read().split()[0:3]
    else:
        load = [int(random.random() * 100600) / 100 for _ in range(3)]
    return {'load1': load[0], 'load5': load[1],}




    @app.context_processor
def inject_load():
    THEPRICE = 0
    def get_price(coin, currency):
        try:
            response = requests.get(URL.format(coin, currency)).json()
            return response
        except:
            return False
    def StartCollection():
        date_time = datetime.now()
        date_time = date_time.strftime("%d/%m/%y %H:%M:%S")
        currentPrice = get_price("BTC", "USD")
        if currentPrice:
            global THEPRICE
            THEPRICE = (currentPrice["USD"])
    StartCollection()
    return {'load1': THEPRICE,}
    '''