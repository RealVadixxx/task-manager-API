import logging

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, OperationalError

from src.database.db import new_session
from src.database.models import TaskDB

from src.schemas.task import TaskSchema, TaskCreate, TaskGet, TaskRename, TaskDelete

logger = logging.getLogger("task_manager")


# [Create] Create task
async def create_task(task: TaskCreate) -> bool:
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

async def get_task(task: TaskGet) -> TaskSchema | None:
    async with new_session() as session:
        try:
            action = await session.get(TaskDB, task.id)
            if action:
                logger.info(f"DB | Get Task | Task: {task.id}")
                return TaskSchema(id = task.id, name = action.name)
            else:
                raise IntegrityError
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return None
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return None
        

# [Update] Rename task
async def rename_task(task: TaskRename) -> bool:
    async with new_session() as session:
        try:
            query = await session.get(TaskDB, task.id)
            if task:
                old_name = query.name
                new_name = task.name
                query.name = task.name

                await session.commit()
                logger.info(f"DB | Rename Task | ID: {task.id} | Name: {old_name} -> {new_name}")
                return True

            else:
                logger.error(f"DB | Rename Task | Task #{task.id} not found")
                return False
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False

# [Delete] Delete task
async def delete_task(task: TaskDelete) -> bool:
    async with new_session() as session:
        try:
            task = await session.get(TaskDB, task.id)
            if task:
                await session.delete(task)

                await session.commit()
                logger.info(f"DB | Delete Task | Task: {task.id}")
                return True
            else:
                print(f"Task #{task.id} not found")
                return False
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False