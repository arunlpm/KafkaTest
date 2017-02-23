import time
import requests
import json
import sys
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')

for response in sys.stdin:
    responseJson = json.loads(response)
    content = responseJson["html"]
    host = responseJson["url"]
    producer.send(host, json.dumps(content).encode('utf-8'), host.encode('utf-8'))