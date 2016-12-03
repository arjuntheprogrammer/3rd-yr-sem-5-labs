import urllib
import urllib2

url = 'http://172.16.68.6:8090/httpclient.html'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
#values = {'username': '14103144',
#          'password': 'hhh',
#          }

values={ 'mode':'191', 'username': '14103144', 'password':'hamla', 'a':'472387474041', 'producttype':'0'}

#headers = {'User-Agent': user_agent}

headers={
'Host': '172.16.68.6:8090'
#User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0
'Accept':text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
'Accept-Language': en-US,en;q=0.5
'Accept-Encoding': gzip, deflate
'Content-Type': application/x-www-form-urlencoded
'Referer': http://172.16.68.6:8090/
'Content-Length': 71
'Connection': keep-alive

}

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
