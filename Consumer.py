from kafka import KafkaConsumer
import lxml.html
from lxml.cssselect import CSSSelector

def run():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest')
    consumer.subscribe(['www.shopclues.com','www.snapdeal.com'])
    return consumer

def main():
	topics = run()
	for each in topics:
		tree = lxml.html.fromstring(each[6])
		sel = CSSSelector('h1')
		results = sel(tree)
		print results[0].text

if __name__ == "__main__":
	main()



