import requests
r = requests.get("http://172.16.68.6:8090/httpclient.html")
#print r.status_code
#print r.headers
print r.content