import os
from dotenv import load_dotenv

import requests as rq

from schemas.task import TaskSchema

load_dotenv()
host = os.getenv("host")

def create_task(task_name: str) -> list:
    url = f"{host}/tasks/create"
    params = {
        "task_name": task_name
    }
    try:
        response = rq.post(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []

def get_tasks() -> list:
    url = f"{host}/tasks/get"
    params = {

    }
    try:
        response = rq.get(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []

def get_task(task_id: int):
    url = f"{host}/tasks/get"
    params = {
        "task_id": task_id
    }
    try:
        response = rq.post(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []

def rename_task(task_id: int, task_name: str) -> list:
    url = f"{host}/tasks/edit/rename"
    params = {
        "task_id": task_id,
        "task_name": task_name
    }
    try:
        response = rq.patch(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []

def delete_task(task_id: int) -> list:
    url = f"{host}/tasks/delete"
    params = {
        "task_id": task_id
    }
    try:
        response = rq.delete(url = url, params = params)
        return response.json()[0]
    except Exception as e:
        print("Something went wrong: {e}")
        return []


