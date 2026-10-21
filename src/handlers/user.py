from fastapi import APIRouter, HTTPException, status

from database.task_user import delete_user as delete_my_user_taskuser
from database.task_user import get_tasks_by_user as get_my_tasks_by_user
from database.user import (
    create_user as create_my_user,
)
from database.user import (
    delete_user as delete_my_user,
)
from database.user import (
    get_user as get_my_user,
)
from database.user import (
    get_users as get_my_users,
)
from database.user import (
    rename_user as rename_my_user,
)
from schemas.user import UserSchema

router = APIRouter()

# Create
@router.post("/users/create")
async def create_user(user_name: str):
    try:
        user = UserSchema(name = user_name)
        action = await (create_my_user(user))
        if action:
            return action
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server error")
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Read
@router.get("/users")
async def get_users():
    try:
        action = await (get_my_users()) # get_my_users = database.user.get_users

        if action:
            return action

    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

@router.get("/users/get")
async def get_user(user_id: int):
    try:
        user = await get_my_user(user_id)

        if user:
            return user
    except: 
        ...    

# Update
@router.patch("/users/edit/rename")
async def rename_user(user_id: int, user_name: str):
    try:
        action = await (rename_my_user(user_id, user_name)) # rename_my_user = database.task.rename_user
        if action:
            return action
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR


# Delete
@router.delete("/users/delete")
async def delete_user(user_id: int):
    try:
        action = await (delete_my_user(user_id)) and await delete_my_user_taskuser(user_id)
        if action:
            return action
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR