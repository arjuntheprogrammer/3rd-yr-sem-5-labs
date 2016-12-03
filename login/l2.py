import requests
data = {'username':'14103144', 'password': 'haml'}
r = requests.get("http://172.16.68.6:8090/httpclient.html", params=data  )
#r = requests.get('http://172.16.68.6:8090/httpclient.html')

#print r.raw

print(r.json)
print(r.url)
print r.status_code
print r.headers
print r.content
#r = requests.post('http://httpbin.org/post', params=data = {'key':'value'})


