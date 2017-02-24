from kafka import KafkaConsumer
from bs4 import BeautifulSoup
import json
import re

class Product:
	def __init__(self, title, price, host):
		self.title = clean(title)
		self.price = price
		self.site = host

def receive():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest')
    consumer.subscribe(['www.shopclues.com','www.snapdeal.com'])
    return consumer

def extract(domhtml, host):
	parser = getParser(host)
	title = domhtml.find(parser["title"]["tag"]).text
	price = domhtml.find(parser["price"]["tag"], parser["price"]["attr"]).text
	return Product(title, price, host)

def getParser(host):
	file = open("parsers.json","r")
	jsonContent = file.read()
	parsers = json.loads(jsonContent)
	return parsers[host]

def clean(value):
	value = value.rstrip()
	value = re.sub('\s+', '', value)
	return value

def main():
	topics = receive()
	for topic in topics:
		payload = json.loads(topic.value)
		dom = BeautifulSoup(payload["html"], "html.parser")
		return extract(dom, topic.key)

if __name__ == "__main__":
	product = main()
	print product.site+"\n" + "Title : "+product.title +"\n"+ "Price : "+product.price+"\n"
