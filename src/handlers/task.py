from fastapi import APIRouter, status

from database.task import create_task as create_my_task
from database.task import delete_task as delete_my_task
from database.task import get_task as get_my_task
from database.task import get_tasks as get_my_tasks
from database.task import rename_task as rename_my_task
from database.task_user import delete_task as delete_my_task_taskuser
from schemas.task import TaskSchema

router = APIRouter()

# Create
@router.post("/tasks/create")
async def create_task(user_name: str):
    try:
        task = TaskSchema(name = user_name)
        action = await create_my_task(task)
        if action:
            return action
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

@router.get("/tasks/get")
async def get_task(task_id: int):
    try:
        task = await get_my_task(task_id)

        if task:
            return task
    except: 
        ...

# Update
@router.patch("/tasks/edit/rename")
async def rename_task(task_id: int, task_name: str):
    try:
        task = await (rename_my_task(task_id, task_name)) # rename_my_task = database.task.rename_task
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
