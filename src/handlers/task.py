import logging

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from src.services import task as svc
from src.schemas.task import TaskCreate, TaskGet, TaskRename, TaskDelete
from src.handlers.tools.message import Ok, OkBut, Created, Error, ValidationError




router = APIRouter()
logger = logging.getLogger("task_manager")

# Create
@router.post("/tasks/create")
async def create_task(task: TaskCreate) -> JSONResponse:
    try:
        action = await svc.create_task(task)
        if action:
            return Created()
        else:
            return Error()
    except RequestValidationError as e:
        logger.warning(f"handlers/task/create_task | Validation Error | {e}")
        return ValidationError()
    except Exception as e:
        logger.critical(f"handlers/task/create_task | Unknown Error | {e}")
        return Error()

# Read
@router.get("/tasks")
async def get_tasks() -> JSONResponse:
    try:
        action = await svc.get_tasks()
        if action:
            result = action
            logger.info(f"API | Get tasks")
            return Ok(result)
        else:
            return OkBut()
    except RequestValidationError as e:
        logger.warning(f"handlers/task/get_tasks | Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST,
                            content = None)
    except Exception as e:
        logger.critical(f"handlers/task/get_tasks | Unknown Error | {e}")
        return Error()

@router.get("/tasks/get")
async def get_task(task: TaskGet) -> JSONResponse:
    try:
        action = await svc.get_task(task)
        if action:
            result = action
            logger.info(f"handlers/task/get_task | ID: {task.id}")
            return Ok(result)
        else:
            return OkBut()
    except RequestValidationError as e:
        logger.warning(f"handlers/task/get_task | Validation Error | {e}")
        return Error()
    except Exception as e:
        logger.critical(f"handlers/task/get_task | Unknown Error | {e}")
        return Error()


# Update
@router.patch("/tasks/edit/rename")
async def rename_task(task: TaskRename) -> JSONResponse:
    try:
        action = await svc.rename_task(task)
        if action:
            logger.info(f"handlers/task/rename_task | ID: {task.id}, New name: {task.new_name}")
            return Ok()
        else:
            raise Exception("No 'action'")
    except RequestValidationError as e:
        logger.warning(f"handlers/task/rename_task | Validation Error | {e}")
        return Error()
    except Exception as e:
        logger.critical(f"handlers/task/rename_task | Unknown Error | {e}")
        return Error()


# Delete
@router.delete("/tasks/delete")
async def delete_task(task: TaskDelete) -> JSONResponse:
    try:
        action = svc.delete_task(task)
        if action:
            logger.info(f"handlers/task/rename_task | ID: {task.id}")
            return Ok()
        else:
            raise Exception("No 'action'")
    except RequestValidationError as e:
        logger.warning(f"handlers/task/delete_task | Validation Error | {e}")
        return Error()
    except Exception as e:
        logger.critical(f"handlers/task/delete_task | Unknown Error | {e}")
        return Error()

