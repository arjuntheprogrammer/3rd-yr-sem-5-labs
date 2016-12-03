import requests

URL = 'http://172.16.68.6:8090/httpclient.html'

data1 = {'username':'14103144', 'password': 'hamla'}

payload = {
    'barcode': 'your user name/login',
    'telephone_primary': 'your password',
    'persistent': '1'  # remember me
}

session = requests.session()
r = requests.get(URL, data=data1)
print r.url



http://172.16.68.6:8090/httpclient.html