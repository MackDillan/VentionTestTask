import requests
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:8000/api-auth/login/'
username = 'admin'
password = 'admin'

new_data = {'name': 'test2'}
valid_data = {'name': 'test'}
req_url = 'http://127.0.0.1:8000/apiCategories/'
response = requests.get(url, auth=HTTPBasicAuth(username, password))


def create_сategory_model():
    resp = requests.post(req_url, data=new_data, auth=HTTPBasicAuth(username, password))
    print(resp.content)


def retrieve_сategory_model():
    resp = requests.get(f'{req_url}{2}/', auth=HTTPBasicAuth(username, password))
    print(resp.content)


def update_сategory_model():
    response = requests.put(f'{req_url}{2}/', valid_data, auth=HTTPBasicAuth(username, password))
    print(response.content)


create_сategory_model()
create_сategory_model()
retrieve_сategory_model()
update_сategory_model()