# import requests


# login_url = "http://127.0.0.1:8000/login"

# login_data = {"username": "testuser", "password": "testpass"}

# res = requests.post(
#     login_url, json=login_data
# )  # to JSON format / get response {'success': True}

# saved_cookies = res.cookies
# # print(saved_cookies)

# # parses the JSON response into a Python dictionary
# if res.json().get("success"):  # {'success': True} -> True
#     print("Login Successful")
# else:
#     print("Login Failed")


# # * request.get_json() (Server-side in Flask)
# # * res.json.get("success") (Client-side in requests):


# protected_url = "http://127.0.0.1:8000/protected"

# res = requests.get(protected_url, cookies=saved_cookies)
# # res = requests.get(protected_url)

# if res.json().get("access"):
#     print("Access Granted")
# else:
#     print("Access Denied")


# ------------------------------------------------------------------------------------


import requests


s = requests.session()

login_url = "http://127.0.0.1:8000/login"

login_data = {"username": "testuser", "password": "testpass"}

res = s.post(login_url, json=login_data)

# saved_cookies = res.cookies
# print(saved_cookies)

if res.json().get("success"):
    print("Login Successful")
else:
    print("Login Failed")


protected_url = "http://127.0.0.1:8000/protected"

# res = s.get(protected_url, cookies=saved_cookies)
res = s.get(protected_url)

if res.json().get("access"):
    print("Access Granted")
else:
    print("Access Denied")
