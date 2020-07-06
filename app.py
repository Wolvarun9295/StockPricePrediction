from flask import Flask, render_template, make_response
from datetime import datetime
import time
import json
import Consumer
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    try:
        pred_price, actual_price, date_time = Consumer.StockPricePrediction(Consumer.LoadModel)
        date_time = int(datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S').strftime('%s')) * 1000
        data = [date_time, pred_price, actual_price]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        time.sleep(2)
        return response
    except:
        print("Response Unsuccessful!")
        sys.exit(1)


if __name__ == ("__main__"):
    app.run(debug=True, host='127.0.0.1', port=5000, passthrough_errors=True)
