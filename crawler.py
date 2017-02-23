import sys
import requests
import json 
from urlparse import urlparse

for url in sys.stdin:
	url = url.strip()
	html = requests.get(url)
	payload = {"url": urlparse(url).netloc, "html":html.text}
	print json.dumps(payload)
