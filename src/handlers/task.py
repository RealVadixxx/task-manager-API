from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException, RequestValidationError
import logging

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
logger = logging.getLogger("task_manager")

# Create
@router.post("/tasks/create")
async def create_task(task_name: str) -> JSONResponse:
    try:
        task = TaskSchema(name = task_name)
        action = await create_my_task(task)
        if action:
            logger.info(f"API | Create task | Name: {task_name}")
            return message.Ok()
        else:
            raise Exception("Create Task")
    except RequestValidationError as e:
        logger.warning(f"Create Task Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST,
                            content = None)
    except Exception as e:
        logger.critical(f"Create Task Unknown Error | {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=None)

# Read
@router.get("/tasks")
async def get_tasks() -> JSONResponse:
    try:
        task = await (get_my_tasks())

        if task:
            logger.info(f"API | Get tasks")
            return message.Ok(task)
        elif task == []:
            logger.info(f"API | Get tasks")
            return message.OkBut()
        else:
            raise Exception("Get_Task")
    except RequestValidationError as e:
        logger.warning(f"Get Tasks Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST,
                            content = None)
    except Exception as e:
        logger.critical(f"Get Tasks Unknown Error | {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=None)

@router.get("/tasks/get")
async def get_task(task_id: int) -> JSONResponse:
    try:
        task = await get_my_task(task_id)

        if task:
            logger.info(f"API | Get task | ID: {task_id}")
            return message.Ok(task.model_dump())
        else:
            raise TaskError("get_task")
    except RequestValidationError as e:
        logger.warning(f"Get Task Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST,
                            content = None)
    except Exception as e:
        logger.critical(f"Get  Task Unknown Error | {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=None)


# Update
@router.patch("/tasks/edit/rename")
async def rename_task(task_id: int, task_name: str) -> JSONResponse:
    try:
        task = await (rename_my_task(task_id, task_name)) # rename_my_task = database.task.rename_task
        if task:
            logger.info(f"API | Rename task | ID: {task_id}")
            return message.Ok()
        else:
            raise TaskError("rename_task")
    except RequestValidationError as e:
        logger.warning(f"Rename Task Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REHTTP_500_INTERNAL_SERVER_ERROR,
                            content = None)
    except Exception as e:
        logger.critical(f"Rename Task Unknown Error | {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=None)


# Delete
@router.delete("/tasks/delete")
async def delete_task(task_id: int) -> JSONResponse:
    try:
        task = await (delete_my_task(task_id)) and await delete_my_task_taskuser(task_id)
        if task:
            logger.info(f"API | Delete task | ID: {task_id}")
            return message.Ok()
        else:
            raise TaskError("delete_task")
    except RequestValidationError as e:
        logger.warning(f"Delete Task Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST,
                            content = None)
    except Exception as e:
        logger.critical(f"Delete Task Unknown Error | {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=None)

