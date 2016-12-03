import urllib

req = urllib.request.Request('http://172.16.68.6:8090/httpclient.html')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
print the_page   