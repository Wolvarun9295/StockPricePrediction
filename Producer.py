from time import sleep
from kafka import KafkaProducer
from alpha_vantage.timeseries import TimeSeries
import random
import json
import sys


def dataGrabber():
    try:
        ticker = 'GOOGL'
        lines = open('key.txt').read().splitlines()
        keys = random.choice(lines)
        time = TimeSeries(key=keys, output_format='json')
        data, metadata = time.get_intraday(symbol=ticker, interval='1min', outputsize='full')
        return data
    except Exception:
        print("Invalid Key!")
        sys.exit(1)


def messagePublisher(producerKey, key, data_key):
    keyBytes = bytes(key, encoding='utf-8')
    producerKey.send("GoogleStock", json.dumps(data[key]).encode('utf-8'), keyBytes)
    print("Message Published!")


def kafkaProducerConnect():
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        return producer
    except Exception:
        print("Connection Refused!")


if __name__ == "__main__":
    data = dataGrabber()
    if len(data) > 0:
        kafkaProducer = kafkaProducerConnect()
        for key in sorted(data):
            messagePublisher(kafkaProducer, key, data[key])
            sleep(3)
