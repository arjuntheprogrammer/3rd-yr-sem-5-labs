import requests
from lxml import etree
data1 = {'mode':'191','username':'14103144', 'password': 'hamla', 'a':'1472387474041', 'producttype':'0'}

headers = {
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded',
'Referer': 'http://172.16.68.6:8090/',
'Content-Length': '70',
'Connection': 'keep-alive'
}

r = requests.get("http://172.16.68.6:8090/login.xml", headers=headers, data=data1  )
#r = requests.get('http://172.16.68.6:8090/httpclient.html')


file = open("out.xml", "w")
file.write(r.content)
file.close()

"""
print r.raw

print(r.json)
print(r.url)
print r.status_code
"""
#print r.headers
ff=r.content

"""
f = etree.fromstring(ff)
for s in f.xpath("//message"):
    print s.text
"""

import xml.etree.ElementTree as ET

tree = ET.parse('out.xml') 
print tree

print ff.find("ccess", 0)
#r = requests.post('http://httpbin.org/post', params=data = {'key':'value'})


#mode=191&username=14103144&password=hamla&a=1472387474041&producttype=0