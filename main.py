import requests
from datetime import datetime


endpoint = 'https://pixe.la/v1/users'
data = '/v1/users/<username>/graphs'
TOKEN = '*******************'
USERNAME = '*******'

user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=endpoint, json=user_parameters)
# print(response.text)

# Creating an account on pixe.la
graph_endpoint = f'{endpoint}/{USERNAME}/graphs'
graph_params = {
    'id': 'code',
    'name': 'Coding Time Graph',
    'unit': 'minutes',
    'type': 'float',
    'color': 'momiji',
}

graph_headers = {
    'X-USER-TOKEN': TOKEN
}
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
# print(graph_response.text)

my_graph_url = ' https://pixe.la/v1/users/teejay/graphs/code.html '

# Posting a pixel

today_date = datetime.now()
today_date = today_date.strftime('%Y%m%d')

# Getting yesterday date
yesterday = datetime(year=2022, month=12, day=5).strftime('%Y%m%d')


post_enpoint = 'https://pixe.la/v1/users/teejay/graphs/code'
post_parameters = {
    'date': today_date,
    'quantity': input("How many minute of coding did you do todays? "),
}

post_response = requests.post(url=post_enpoint, json=post_parameters, headers=graph_headers)
print(post_response.text)

# Working with the put requests
put_endpoint = f'https://pixe.la/v1/users/teejay/graphs/code/{yesterday}'
put_parameters = {
    'quantity': '127.24',
}
# put_response = requests.put(url=put_endpoint, json=put_parameters, headers=graph_headers)
# print(put_response.text)

# Working with the delete requests
delete_endpoint = f'https://pixe.la/v1/users/teejay/graphs/code/{today_date}'
delete_header = {
    'X-USER-TOKEN': TOKEN,
}
# delete_response = requests.delete(url=delete_endpoint, headers=delete_header)
# print(delete_response.text)