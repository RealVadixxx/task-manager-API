from sqlalchemy import delete, select

from database.db import new_session
from database.models import TaskDB, TaskUserDB, UserDB
from schemas.task import TaskSchema
from schemas.user import UserSchema


# [Create] Add user to task
async def add_user2task(user_id: int, task_id: int) -> bool:
    async with new_session() as session:
        try:
            new_user_task = TaskUserDB(user_id = user_id, task_id = task_id)
            session.add(new_user_task)
            await session.commit()

            return True
        except:
            print(e)
            return False

# [Read] Get users, where task == ...
async def get_users_by_task(task_id: int) -> list[UserSchema] | None:
    async with new_session() as session:
        try:
            query = (
                select(UserDB)
                .join(TaskUserDB, UserDB.id == TaskUserDB.user_id)
                .where(TaskUserDB.task_id == task_id)
            )
            query_result = await session.execute(query)
            data = query_result.scalars().all()

            result = [UserSchema(id = link.id, name = link.name) for link in data]

            return result
        except Exception as e:
            print(e)
            return None
            

# [Read] Get tasks, where user == ...
async def get_tasks_by_user(user_id: int) -> list[TaskSchema] | None:
    async with new_session() as session:
        try:
            query = (
                select(TaskDB)
                .join(TaskUserDB, TaskDB.id == TaskUserDB.task_id)
                .where(TaskUserDB.user_id == user_id)
            )
            query_result = await session.execute(query)
            data = query_result.scalars().all()

            result = [TaskSchema(id = link.id, name = link.name) for link in data]

            return result
        except Exception as e:
            print(e)
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

            return True
    
        except Exception as e:
            print(e)
            return False

# [Delete] Delete task
async def delete_task(task_id: int) -> bool:
    async with new_session() as session:
        stmt = delete(TaskUserDB).where(TaskUserDB.task_id == task_id)
        try:
            await session.execute(stmt)
            await session.commit()
            return True
        except Exception as e:
            print(e)
            return False

# [Delete] Remove user
async def delete_user(user_id: int) -> bool:
    async with new_session() as session:
        stmt = delete(TaskUserDB).where(TaskUserDB.user_id == user_id)
        try:
            await session.execute(stmt)
            await session.commit()
            return True
        except Exception as e:
            print(e)
            return False