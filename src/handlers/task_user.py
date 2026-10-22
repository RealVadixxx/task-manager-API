from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.task_user import (
    add_user2task as add_my_user2task,
    remove_user_in_task as remove_my_user_in_task,
    get_tasks_by_user as get_my_tasks_by_user,
    get_users_by_task as get_my_users_by_task
)
from handlers.tools import message
from handlers.tools.exceptions import TaskUserError

router = APIRouter()


# Create
@router.patch("/tasks/edit/users/add")
async def add_user2task(user_id: int, task_id: int) -> JSONResponse:
    try:
        task = await (add_my_user2task(user_id, task_id))
        if task:
            return message.Ok()
        else:
            raise TaskUserError("add_user2task: No task")
    except Exception as e:
        print(e)
        return message.Error()

# Read
@router.get("/tasks/users")
async def get_users_by_task(task_id: int) -> JSONResponse:
    """ Get users by task """
    try:
        task = await get_my_users_by_task(task_id)
        if task:
            return message.Ok(task)
        elif task == []:
            return message.OkBut()
        else:
             raise TaskUserError("get_users_by_task: No users")
    except Exception as e:
        print(e)
        return message.Error()

# Read
@router.get("/users/tasks")
async def get_tasks_by_user(user_id: int) -> JSONResponse:
    try:
        task = await get_my_tasks_by_user(user_id)
        if task:
            return message.Ok(task)
        elif task == []: 
            return message.OkBut()
        else:
            raise TaskUserError("get_tasks_by_user: No tasks")
    except Exception as e:
        print(e)
        return message.Error()
    
# Update / Delete
@router.patch("/tasks/edit/users/remove")
async def remove_user2task(user_id: int, task_id: int) -> JSONResponse:
    try:
        task = await (remove_my_user_in_task(user_id, task_id))
        if task:
            return message.Ok()
        else:
            raise TaskUserError("remove_user2task: No data?")
    except Exception as e:
        print(e)
        return message.Error()

