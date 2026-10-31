import logging
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError, OperationalError

from database.db import new_session
from database.models import TaskDB, TaskUserDB, UserDB
from schemas.task import TaskSchema
from schemas.user import UserSchema

logger = logging.getLogger("task_manager")

# [Create] Add user to task
async def add_user2task(user_id: int, task_id: int) -> bool:
    async with new_session() as session:
        try:
            new_user_task = TaskUserDB(user_id = user_id, task_id = task_id)
            session.add(new_user_task)
            await session.commit()
            logger.info(f"DB | Add User to Task | uid: {user_id} | task_id: {task_id}")
            return True
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False

# [Read] Get users, where task == ...
async def get_users_by_task(task_id: int) -> list | None:
    async with new_session() as session:
        try:
            query = (
                select(UserDB)
                .join(TaskUserDB, UserDB.id == TaskUserDB.user_id)
                .where(TaskUserDB.task_id == task_id)
            )
            query_result = await session.execute(query)
            data = query_result.scalars().all()

            result = [UserSchema(id = link.id, name = link.name).model_dump() for link in data]
            logger.info(f"DB | Get Users by Task | task_id: {task_id}")
            return result
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return None
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return None
            

# [Read] Get tasks, where user == ...
async def get_tasks_by_user(user_id: int) -> list | None:
    async with new_session() as session:
        try:
            query = (
                select(TaskDB)
                .join(TaskUserDB, TaskDB.id == TaskUserDB.task_id)
                .where(TaskUserDB.user_id == user_id)
            )
            query_result = await session.execute(query)
            data = query_result.scalars().all()

            result = [TaskSchema(id = link.id, name = link.name).model_dump() for link in data]
            logger.info(f"DB | Get Tasks by User | uid: {user_id}")
            return result
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return None
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return None

# [Delete] Remove user in task
async def remove_user_in_task(user_id_to_remove: int, task_id_to_remove: int) -> bool:
    async with new_session() as session:
        try:
            stmt = delete(TaskUserDB).where(
                TaskUserDB.user_id == user_id_to_remove,
                TaskUserDB.task_id == task_id_to_remove
            )
            await session.execute(stmt)
            await session.commit()
            logger.info(f"DB | Remove User in Task | uid: {user_id_to_remove} | task_id: {task_id_to_remove}")
            return True
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
        stmt = delete(TaskUserDB).where(TaskUserDB.task_id == task_id)
        try:
            await session.execute(stmt)
            await session.commit()
            logger.info(f"DB | Delete task | task_id: {task_id}")
            return True
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False

# [Delete] Remove user
async def delete_user(user_id: int) -> bool:
    async with new_session() as session:
        stmt = delete(TaskUserDB).where(TaskUserDB.user_id == user_id)
        try:
            await session.execute(stmt)
            await session.commit()
            logger.info(f"DB | Delete user | uid: {user_id}")
            return True
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False