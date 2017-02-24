import time
import requests
import json
import sys
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')

for response in sys.stdin:
    responseJson = json.loads(response)
    host = responseJson["url"]
    producer.send(host, response, host.encode('utf-8'))