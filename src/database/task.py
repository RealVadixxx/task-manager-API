import logging

from sqlalchemy.exc import IntegrityError, OperationalError
from database.db import new_session
from sqlalchemy import select
from database.models import TaskDB
from schemas.task import TaskSchema

logger = logging.getLogger("task_manager")


# [Create] Create task
async def create_task(task: TaskSchema) -> bool:
    async with new_session() as session:
        try:
            session.add(TaskDB(name = task.name))
            await session.commit()
            logger.info(f"DB | Create Task | Name: {task.name}")
            return True
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False

# [Read] Get all tasks
async def get_tasks() -> list | None:
    async with new_session() as session:
        try:
            tasks = await session.scalars(select(TaskDB))
            tasks = tasks.all()
            result = [TaskSchema(id = task.id, name = task.name).model_dump() for task in tasks]
            logger.info(f"DB | Get Tasks")
            if result == [] or result:
                return result
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False

async def get_task(task_id) -> TaskSchema | None:
    async with new_session() as session:
        try:
            task = await session.get(TaskDB, task_id)
            if task:
                logger.info(f"DB | Get Task | Task: {task.id, task.name}")
                return TaskSchema(id = task.id, name = task.name)
            else:
                raise IntegrityError
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False
        

# [Update] Rename task
async def rename_task(task_id: int, new_name: str) -> bool:
    async with new_session() as session:
        try:
            task = await session.get(TaskDB, task_id)
            old_name = task.name
            if task:
                task.name = new_name

                await session.commit()
                logger.info(f"DB | Rename Task | ID: {task_id} | Name: {old_name} -> {task.name}")
                return True

            else:
                print(f"Task #{task_id} not found")
                return False
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False

# [Delete] Delete task
async def delete_task(task_id: int) -> bool:
    async with new_session() as session:
        try:
            task = await session.get(TaskDB, task_id)
            task_name = task.name
            if task:
                await session.delete(task)

                await session.commit()
                logger.info(f"DB | Delete Task | Task: {task_id, task_name}")
                return True
            else:
                print(f"Task #{task_id} not found")
                return False
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False