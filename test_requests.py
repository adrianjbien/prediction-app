import requests

# GET method test
url = 'http://localhost:5000/api/data'
response = requests.get(url)
print(response.text)



# POST method test success
url = 'http://localhost:5000/api/data'
myobj = {'x' : '1.4',
         'y' : '1.4',
         'cat' : '3'}
response = requests.post(url, json=myobj)
print(response.text)



# # POST method test failure
url = 'http://localhost:5000/api/data'
myobj = {'x' : '1.4',
         'y' : '1.4',
         'cat' : "dog"}
response = requests.post(url, json=myobj)
print(response.text)



# DELETE method test success
url = 'http://localhost:5000/api/data/1'
response = requests.delete(url)
print(response.text)



# DELETE method test failure
url = 'http://localhost:5000/api/data/100'
response = requests.delete(url)
print(response.text)