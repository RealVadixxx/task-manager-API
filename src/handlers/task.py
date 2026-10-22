from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from database.task import create_task as create_my_task
from database.task import delete_task as delete_my_task
from database.task import get_task as get_my_task
from database.task import get_tasks as get_my_tasks
from database.task import rename_task as rename_my_task
from database.task_user import delete_task as delete_my_task_taskuser
from schemas.task import TaskSchema

from handlers.tools import message
from handlers.tools.exceptions import UserError
from handlers.tools.exceptions import TaskError
router = APIRouter()

# Create
@router.post("/tasks/create")
async def create_task(task_name: str) -> JSONResponse:
    try:
        task = TaskSchema(name = task_name)
        action = await create_my_task(task)
        if action:
            return message.Ok()
        else:
            raise UserError("create_task: error")
    except Exception as e:
        print(e)
        return message.Error()

# Read
@router.get("/tasks")
async def get_tasks() -> JSONResponse:
    try:
        task = await (get_my_tasks())

        if task:
            return message.Ok(task)
        elif task == []: 
            return message.OkBut()
        else:
            raise UserError("get_tasks: error")
    except Exception as e:
        print(e)
        return message.Error()

@router.get("/tasks/get")
async def get_task(task_id: int) -> JSONResponse:
    try:
        task = await get_my_task(task_id)

        if task:
            return message.Ok(task.model_dump())
        else:
            raise TaskError("get_task")
    except Exception as e:
        print(e)
        return message.Error()

# Update
@router.patch("/tasks/edit/rename")
async def rename_task(task_id: int, task_name: str) -> JSONResponse:
    try:
        task = await (rename_my_task(task_id, task_name)) # rename_my_task = database.task.rename_task
        if task:
            return message.Ok()
        else:
            raise TaskError("rename_task")
    except Exception as e: 
        print(e)
        return message.Error()

# Delete
@router.delete("/tasks/delete")
async def delete_task(task_id: int) -> JSONResponse:
    try:
        task = await (delete_my_task(task_id)) and await delete_my_task_taskuser(task_id)
        if task:
            return message.Ok()
        else:
            raise TaskError("delete_task")
    except Exception as e: 
        print(e)
        return message.Error()
