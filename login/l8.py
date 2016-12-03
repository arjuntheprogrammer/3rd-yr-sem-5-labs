
import urllib2
print urllib2.urlopen("http://172.16.68.6:8090/httpclient.html").read()



import urllib2
req = urllib2.Request(url='http://172.16.68.6:8090/httpclient.html',
                       data={'username': '14103144',
          'password': 'hhh',
          })
f = urllib2.urlopen(req)
print f.read()