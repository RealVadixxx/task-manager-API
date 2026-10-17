from fastapi import APIRouter, status, Response
from database.task import (
    create_task as create_my_task,
    get_tasks as get_my_tasks,
    rename_task as rename_my_task,
    delete_task as delete_my_task
)
from database.task_user import (
    add_user2task as add_my_user2task,
    remove_user_in_task as remove_my_user_in_task
)
import asyncio

router = APIRouter()

# Create
@router.post("/tasks/create")
async def create_task(name: str):
    try:
        task = asyncio.create_task(create_my_task(name))
        if task.result:
            return Response(
                content = get_tasks(),
                status_code = status.HTTP_201_CREATED
            )
    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Read
@router.get("/tasks")
async def get_tasks():
    try:
        task = asyncio.create_task(get_my_tasks()) # get_my_tasks = database.task.get_tasks

        if task.result():
            return Response(
                content = task.result(),
                status_code = status.HTTP_200_OK
            )

    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Update
@router.patch("/tasks/edit/rename")
async def rename_task(task_id: int, new_name: str):
    try:
        task = asyncio.create_task(rename_my_task(task_id, new_name)) # rename_my_task = database.task.rename_task
        if task.result():
            return Response(
                content = get_tasks(),
                status_code = status.HTTP_200_OK
            )
    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Update
@router.patch("/tasks/edit/users/add")
async def add_user2task(user_id: int, task_id: int):
    try:
        task = asyncio.create_task(add_my_user2task(user_id, task_id))
        if task.result():
            return Response(
                content=get_tasks(),
                status_code=status.HTTP_200_OK
            )
    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Update
@router.patch("/tasks/edit/users/remove")
async def remove_user2task(user_id: int, task_id: int):
    try:
        task = asyncio.create_task(remove_my_user_in_task(user_id, task_id))
        if task.result():
            return Response(
                content=get_tasks(),
                status_code=status.HTTP_200_OK
            )
    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR


# Delete
@router.delete("/tasks/delete")
async def delete_task(task_id: int):
    try:
        task = asyncio.create_task(delete_my_task(task_id))
        if task.result():
            return Response(
                content = get_tasks(),
                status_code = status.HTTP_200_OK
            )
    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR
