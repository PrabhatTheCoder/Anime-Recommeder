import requests

# Login to get tokens
resp = requests.post('http://172.16.2.44/auth/login/', data={
    "email": "admin@gmail.com",
    "password": "admin"
})
tokens = resp.json()
access = tokens['access']
refresh = tokens['refresh']
print("access :", access)
print("refresh :", refresh)

# Use access token in API call
headers = {'Authorization': f'Bearer {access}'}
response = requests.get('http://172.16.2.44/user/list-preferences/', headers=headers)

print(response.status_code)
print(response.json())

# If access token expires
# refresh_resp = requests.post('http://172.16.2.44/api/token/refresh/', json={'refresh': refresh})
# new_access = refresh_resp.json()['access']
