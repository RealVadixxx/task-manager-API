from fastapi import APIRouter, status, Response
from database.task import (
    create_task as create_my_task,
    get_tasks as get_my_tasks,
    rename_task as rename_my_task,
    delete_task as delete_my_task
)
from database.task_user import (
    add_user2task as add_my_user2task,
    remove_user_in_task as remove_my_user_in_task,
    delete_task as delete_my_task_taskuser,
)
import asyncio

router = APIRouter()

# Create
@router.post("/tasks/create")
async def create_task(name: str):
    try:
        task = await (create_my_task(name))
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Read
@router.get("/tasks")
async def get_tasks():
    try:
        task = await (get_my_tasks()) # get_my_tasks = database.task.get_tasks

        if task:
            return task

    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Update
@router.patch("/tasks/edit/rename")
async def rename_task(task_id: int, new_name: str):
    try:
        task = await (rename_my_task(task_id, new_name)) # rename_my_task = database.task.rename_task
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Update
@router.patch("/tasks/edit/users/add")
async def add_user2task(user_id: int, task_id: int):
    try:
        task = await (add_my_user2task(user_id, task_id))
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Update
@router.patch("/tasks/edit/users/remove")
async def remove_user2task(user_id: int, task_id: int):
    try:
        task = await (remove_my_user_in_task(user_id, task_id))
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR


# Delete
@router.delete("/tasks/delete")
async def delete_task(task_id: int):
    try:
        task = await (delete_my_task(task_id)) and await delete_my_task_taskuser(task_id)
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR
