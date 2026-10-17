from fastapi import APIRouter, Response, status
from database.user import (
    create_user as create_my_user,
    get_users as get_my_users,
    rename_user as rename_my_user,
    delete_user as delete_my_user
)
from database.task_user import (
    get_tasks_by_user as get_my_tasks_by_user,
)
import asyncio


router = APIRouter()

# Create
@router.post("/users/create")
async def create_user(name: str):
    try:
        task = asyncio.create_task(create_my_user(name))
        if task.result:
            return Response(
                content = get_users(),
                status_code=status.HTTP_201_CREATED
            )
    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Read
@router.get("/users")
async def get_users():
    try:
        task = asyncio.create_task(get_my_users()) # get_my_users = database.user.get_users

        if task.result():
            return Response(
                content = task.result(),
                status_code = status.HTTP_200_OK
            )

    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

@router.get("/users/tasks")
async def get_tasks_by_user(user_id: int):
    try:
        task = asyncio.create_task(get_my_tasks_by_user(user_id))

        if task.result():
            return Response(
                content = task.result(),
                status_code = status.HTTP_200_OK
            )

    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Update
@router.patch("/users/edit")
async def rename_user(user_id: int, new_name: str):
    try:
        task = asyncio.create_task(rename_my_user(user_id, new_name)) # rename_my_user = database.task.rename_user
        if task.result():
            return Response(
                content = get_users(),
                status_code = status.HTTP_200_OK
            )
    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR


# Delete
@router.delete("/users/delete")
async def delete_user(user_id: int):
    try:
        task = asyncio.create_task(delete_my_user(user_id))
        if task.result():
            return Response(
                content = get_users(),
                status_code = status.HTTP_200_OK
            )
    except Exception as e:
        print("Something went wrong")
        return status.HTTP_500_INTERNAL_SERVER_ERROR