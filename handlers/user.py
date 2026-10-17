from fastapi import APIRouter, Response, status, HTTPException
from starlette.status import HTTP_200_OK

from database.user import (
    create_user as create_my_user,
    get_users as get_my_users,
    rename_user as rename_my_user,
    delete_user as delete_my_user
)
from database.task_user import (
    get_tasks_by_user as get_my_tasks_by_user,
    delete_user as delete_my_user_taskuser
)
import asyncio


router = APIRouter()

# Create
@router.post("/users/create")
async def create_user(name: str):
    try:
        task = await (create_my_user(name))
        if task:
            return task
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server error")
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Read
@router.get("/users")
async def get_users():
    try:
        task = await (get_my_users()) # get_my_users = database.user.get_users

        if task:
            return task

    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

@router.get("/users/tasks")
async def get_tasks_by_user(user_id: int):
    try:
        task = await (get_my_tasks_by_user(user_id))

        if task:
            return task

    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Update
@router.patch("/users/edit")
async def rename_user(user_id: int, new_name: str):
    try:
        task = await (rename_my_user(user_id, new_name)) # rename_my_user = database.task.rename_user
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR


# Delete
@router.delete("/users/delete")
async def delete_user(user_id: int):
    try:
        task = await (delete_my_user(user_id)) and await delete_my_user_taskuser(user_id)
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR