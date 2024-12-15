import requests

url = 'http://localhost:5000/api/data'
myobj = {'x' : '1.4',
         'y' : '1.4',
         'cat' : '3'}

x = requests.post(url, json = myobj)

print(x.text)