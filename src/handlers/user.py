from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

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

from handlers.tools import message
from handlers.tools.exceptions import UserError


router = APIRouter()

# Create
@router.get("/users/create")
async def create_user(user_name: str) -> JSONResponse:
    try:
        user = UserSchema(name = user_name)
        action = await (create_my_user(user))
        if action:
            return message.Ok() # Maybe 'return message.Created()' but I do not wanna this.
        else:
            raise UserError("create_user: Error")
    except Exception as e:
        print(e)
        return message.Error()

# Read
@router.get("/users")
async def get_users() -> JSONResponse:
    try:
        action = await (get_my_users())

        if action:
            users = [UserSchema(id = user.id, name = user.name).model_dump() for user in action] 
            return message.Ok(users)
        elif action == []: 
            return message.OkBut()
        else:
            raise UserError("get_users: error")
    except Exception as e:
        print(e)
        return message.Error()


@router.get("/users/get")
async def get_user(user_id: int) -> JSONResponse:
    try:
        action = await get_my_user(user_id)

        if action:
            user = action.model_dump()
            return message.Ok(user)
        else:
            raise UserError("get_user: error")
    except Exception as e: 
        print(e)
        return message.Error()

# Update
@router.patch("/users/edit/rename")
async def rename_user(user_id: int, user_name: str) -> JSONResponse:
    try:
        action = await (rename_my_user(user_id, user_name)) # rename_my_user = database.task.rename_user
        if action:
            return message.Ok()
        else:
            raise UserError("rename_user: error")
    except Exception as e: 
        print(e)
        return message.Error()


# Delete
@router.delete("/users/delete")
async def delete_user(user_id: int):
    try:
        action = await (delete_my_user(user_id)) and await delete_my_user_taskuser(user_id)
        if action:
            return message.Ok()
        else:
            raise UserError("delete_user: error")
    except Exception as e: 
        print(e)
        return message.Error()
