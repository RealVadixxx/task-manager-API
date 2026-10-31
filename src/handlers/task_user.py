import logging
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


from database.task_user import (
    add_user2task as add_my_user2task,
    remove_user_in_task as remove_my_user_in_task,
    get_tasks_by_user as get_my_tasks_by_user,
    get_users_by_task as get_my_users_by_task
)
from handlers.tools import message
from handlers.tools.exceptions import TaskUserError

router = APIRouter()
logger = logging.getLogger("task_manager")

# Create
@router.patch("/tasks/edit/users/add")
async def add_user2task(user_id: int, task_id: int) -> JSONResponse:
    try:
        task = await (add_my_user2task(user_id, task_id))
        if task:
            logger.info(f"API | Add User to Task | uid: {user_id} | task_id: {task_id}")
            return message.Ok()
        else:
            raise TaskUserError("add_user2task: No task")
    except RequestValidationError as e:
        logger.warning(f"Add User to Task Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST,
                            content = None)
    except Exception as e:
        logger.critical(f"Add User to Task Unknown Error | {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=None)
# Read
@router.get("/tasks/users")
async def get_users_by_task(task_id: int) -> JSONResponse:
    """ Get users by task """
    try:
        task = await get_my_users_by_task(task_id)
        if task:
            logger.info(f"API | Get Users by Task | task_id: {task_id}")
            return message.Ok(task)
        elif task == []:
            return message.OkBut()
        else:
             raise TaskUserError("get_users_by_task: No users")
    except RequestValidationError as e:
        logger.warning(f"Get Users by Task Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST,
                            content = None)
    except Exception as e:
        logger.critical(f"Get Users by Task Unknown Error | {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=None)

# Read
@router.get("/users/tasks")
async def get_tasks_by_user(user_id: int) -> JSONResponse:
    try:
        task = await get_my_tasks_by_user(user_id)
        if task:
            logger.info(f"API | Get Tasks by User | uid: {user_id}")
            return message.Ok(task)
        elif task == []: 
            return message.OkBut()
        else:
            raise Exception("get_tasks_by_user: No tasks")
    except RequestValidationError as e:
        logger.warning(f"Get Tasks by User Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST,
                            content = None)
    except Exception as e:
        logger.critical(f"Get Tasks by User Unknown Error | {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=None)
    
# Update / Delete
@router.patch("/tasks/edit/users/remove")
async def remove_user2task(user_id: int, task_id: int) -> JSONResponse:
    try:
        task = await (remove_my_user_in_task(user_id, task_id))
        if task:
            logger.info(f"API | Remove User from Task | uid: {user_id} | task_id: {task_id}")
            return message.Ok()
        else:
            raise Exception("remove_user2task: No data?")
    except RequestValidationError as e:
        logger.warning(f"Remove User in Task Validation Error | {e}")
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST,
                            content = None)
    except Exception as e:
        logger.critical(f"Remove User in Task Unknown Error | {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=None)