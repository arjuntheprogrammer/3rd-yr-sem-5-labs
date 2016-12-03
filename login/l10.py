import requests

data={ 'mode':'191',
		 'username': '14103144',
		  'password':'hamla', 
		  'a':'472387474041', 
		  'producttype':'0'}

#data = {'username':'14103144', 'password': 'haml'}
r = requests.post("http://172.16.68.6:8090/login.xml", params=data  )
#r = requests.get('http://172.16.68.6:8090/httpclient.html')

print r.raw

print(r.json)
print(r.url)
print r.status_code
print r.headers
print r.content
#r = requests.post('http://httpbin.org/post', params=data = {'key':'value'})


