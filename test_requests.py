import requests
from sklearn.neighbors import KNeighborsClassifier

# # GET method test
# url = 'http://localhost:5000/api/data'
# response = requests.get(url)
# print(response.text)
#
#
#
# # POST method test success
# url = 'http://localhost:5000/api/data'
# myobj = {'x' : '1.4',
#          'y' : '1.4',
#          'cat' : '3'}
# response = requests.post(url, json=myobj)
# print(response.text)
#
#
#
# # # POST method test failure
# url = 'http://localhost:5000/api/data'
# myobj = {'x' : '1.4',
#          'y' : '1.4',
#          'cat' : "dog"}
# response = requests.post(url, json=myobj)
# print(response.text)
#
#
#
# # DELETE method test success
# url = 'http://localhost:5000/api/data/1'
# response = requests.delete(url)
# print(response.text)
#
#
#
# # DELETE method test failure
# url = 'http://localhost:5000/api/data/100'
# response = requests.delete(url)
# print(response.text)

if __name__ == '__main__':
    neigh = KNeighborsClassifier(n_neighbors=3)
    X = [[3.14, 2.56], [3.24, 2.5], [1.12, 3.4], [1.4, 3.11]]
    y = [1, 1, 2, 2]
    neigh.fit(X, y)
    print(neigh.predict([[3.14, 2.56], [1.32, 3.22]]))