import requests
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from app import get_points

# # # GET method test
# url = 'http://localhost:5000/api/data'
# response = requests.get(url)
# print(response.text)
# #
# #
# #
# POST method test success
url = 'http://localhost:5000/api/data'
myobj = {'x' : '1.4',
         'y' : '1.4',
         'cat' : '3'}
response = requests.post(url, json=myobj)
print(response.text)
# #
# #
# #
# # # # POST method test failure
# url = 'http://localhost:5000/api/data'
# myobj = {'x' : '1.4',
#          'y' : '1.4',
#          'cat' : "dog"}
# response = requests.post(url, json=myobj)
# print(response.text)

# #
# #
# # # DELETE method test success
# url = 'http://localhost:5000/api/data/1'
# response = requests.delete(url)
# print(response.text)
# #
# #
# #
# # # DELETE method test failure
# url = 'http://localhost:5000/api/data/100'
# response = requests.delete(url)
# print(response.text)

# if __name__ == '__main__':
#     all_data = get_points()
#     scaler = StandardScaler()
#     data_to_standardize = [[data['x'], data['y']] for data in all_data]
#     categories = [data['cat'] for data in all_data]

#     print("before")
#     print(data_to_standardize)

#     scaler.fit(data_to_standardize)

#     print("after")
#     data_to_standardize = scaler.transform(data_to_standardize)
#     print(data_to_standardize)

