import logging

from src.database.task import create_task as db_create_task
from src.database.task import delete_task as db_delete_task
from src.database.task import get_task as db_get_task
from src.database.task import get_tasks as db_get_tasks
from src.database.task import rename_task as db_rename_task

from src.schemas.task import TaskSchema, TaskCreate, TaskGet, TaskRename, TaskDelete

logger = logging.getLogger("task_manager")

async def create_task(task: TaskCreate) -> bool:
    try:
        action = await db_create_task(task)
        if action:
            return True
        else:
            return False
    except Exception as e:
        logger.critical(f"services/task/create_task | Unknown error: {e}")
        logger.info(f"services/task/create_task | Entered data: {task.name}")
        return False
async def get_tasks() -> list | None:
    try:
        action = await db_get_tasks()
        if action:
            result = action
            return result
        else:
            return None
    except Exception as e:
        logger.critical(f"services/task/get_tasks | Unknown error: {e}")
        return None
async def get_task(task: TaskGet) -> TaskSchema | None:
    try:
        action = await db_get_task(task)
        if action:
            result = action
            return result
        else:
            return None
    except Exception as e:
        logger.critical(f"services/task/get_task | Unknown error: {e}")
        logger.info(f"services/task/get_task | Entered data: {task.id}")
        return None
async def rename_task(task: TaskRename) -> bool:
    try:
        action = await db_rename_task(task)
        if action:
            return True
        else:
            return False
    except Exception as e:
        logger.critical(f"services/task/rename_task | Unknown error: {e}")
        logger.info(f"services/task/rename_task | Entered data: task_id:{task.id};task_name:{task.new_name}")
        return False
async def delete_task(task: TaskDelete) -> bool:
    try:
        action = await db_delete_task(task)
        if action:
            return True
        else:
            return False
    except Exception as e:
        logger.critical(f"services/task/delete_task | Unknown error: {e}")
        logger.info(f"services/task/delete_task | Entered data: task_id:{task.id}")
        return False