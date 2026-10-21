import os
from dotenv import load_dotenv

import requests as rq

from schemas.user import UserSchema

load_dotenv()
host = os.getenv("host")

def create_user(user_name: str) -> list:
    url = f"{host}/users/create"
    params = {
        "user_name": user_name
    }
    try:
        response = rq.post(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []

def get_users() -> list:
    url = f"{host}/users"
    params = {

    }
    try:
        response = rq.get(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []

def get_user(user_id: int):
    url = f"{host}/users/get"
    params = {
        "user_id": user_id
    }
    try:
        response = rq.post(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []

def rename_user(user_id: int, user_name: str) -> list:
    url = f"{host}/users/edit"
    params = {
        "user_name": user_name
    }
    try:
        response = rq.patch(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []

def delete_user(user_id: int) -> list:
    url = f"{host}/users/edit"
    params = {
        "user_id": user_id
    }
    try:
        response = rq.patch(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []