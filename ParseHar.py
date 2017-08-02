#!/usr/bin/env python
import json
import sys
import urllib.request

har_file = sys.argv[1]

har_contents = open(har_file,'r').read()

har = json.loads(har_contents)


matching_entries = filter(lambda x: ".jpg" in x['request']['url'],har['log']['entries'])
matching_urls = set(map(lambda x: x['request']['url'],matching_entries))

count = 0

for url in matching_urls:
   if "7tthpaamkg4rcc30" in url:
       count+=1
       print(url)
       urllib.request.urlretrieve(url,str(count) + ".jpg")
print(count)

