import requests

url = "http://127.0.0.1:8000"

def create_user(user_name: str):
    request_url = url + "/users/create"
    response = requests.post(request_url, user_name)
    response.raise_for_status()
    print(response.json())

create_user("Lol")
