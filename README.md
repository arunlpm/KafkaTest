# KafkaTest
Realtime data extraction

Kafka Version = 2.10.X


How to run:
1. Start zookeeper and kafka server
2. We can start pipeline from terminal using the following commands,
   Producer:
   `cat urls | python crawler.py | python Producer.py`
  
   Consumer:
    `Consumer.py`
    
Input:

    "urls" file has list of urls to crawl.
    
Output: 

    Prints the title and price of the product for the subscribed topics. 
