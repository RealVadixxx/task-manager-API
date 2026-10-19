import os
from dotenv import load_dotenv

import requests as rq


load_dotenv()
host = os.getenv("host")

def get_users_by_task(task_id: int):
    url = f"{host}/tasks/users"
    params = {
        "task_id": task_id,
    }
    try:
        response = rq.get(url = url, params = params)
        return response.json()[0]
    except:
        ...

def get_tasks_by_users(user_id: int):
    url = f"{host}/users/tasks"
    params = {
        "user_id": user_id,
    }
    try:
        response = rq.get(url = url, params = params)
        return response.json()[0]
    except:
        ...

def add_user2task(user_id: int, task_id: int):
    url = f"{host}/tasks/edit/users/add"
    params = {
        "user_id": user_id,
        "task_id": task_id
    }
    try:
        response = rq.patch(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []

def remove_user2task(user_id: int, task_id: int):
    url = f"{host}/tasks/edit/users/remove"
    params = {
        "user_id": user_id,
        "task_id": task_id
    }
    try:
        response = rq.patch(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []