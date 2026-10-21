from sqlalchemy import delete, select

from database.db import new_session
from database.models import TaskDB, TaskUserDB, UserDB
from schemas.task import TaskSchema
from schemas.user import UserSchema


# [Create] Add user to task
async def add_user2task(user_id: int, task_id: int):
    async with new_session() as session:
        new_user_task = TaskUserDB(user_id = user_id, task_id = task_id)
        session.add(new_user_task)
        await session.commit()

        links = await session.scalars(select(TaskUserDB))
        links = links.all()
        result = [{"user.id": link.user_id, "name": link.task_id} for link in links]

        return result

# [Read] Get users, where task == ...
async def get_users_by_task(task_id: int):
    async with new_session() as session:
        query = (
            select(UserDB)
            .join(TaskUserDB, UserDB.id == TaskUserDB.user_id)
            .where(TaskUserDB.task_id == task_id)
        )
        query_result = await session.execute(query)
        data = query_result.scalars().all()

        result = [{"user_id": link.id, "user_name": link.name} for link in data]

        return result

# [Read] Get tasks, where user == ...
async def get_tasks_by_user(user_id: int):
    async with new_session() as session:
        query = (
            select(TaskDB)
            .join(TaskUserDB, TaskDB.id == TaskUserDB.task_id)
            .where(TaskUserDB.user_id == user_id)
        )
        query_result = await session.execute(query)
        data = query_result.scalars().all()

        result = [{"task_id": link.id, "task_name": link.name} for link in data]

        return result

# [Delete] Remove user in task
async def remove_user_in_task(user_id_to_remove: int, task_id_to_remove: int):
    async with new_session() as session:
        task_user_list = await session.get(TaskUserDB, task_id = task_id_to_remove, user_id = user_id_to_remove)

        if task_user_list:
            await session.delete(task_user_list)

            await session.commit()

            links = await session.scalars(select(TaskUserDB))
            links = links.all()
            result = [{"user.id": link.user_id, "name": link.task_id} for link in links]

            return result
        else:
            print("Something went wrong")
            return None

# [Delete] Delete task
async def delete_task(task_id: int):
    async with new_session() as session:
        stmt = delete(TaskUserDB).where(TaskUserDB.task_id == task_id)
        try:
            await session.execute(stmt)
            await session.commit()
            return True
        except Exception as e:
            print(f"{e}")
            return False

# [Delete] Remove user
async def delete_user(user_id: int):
    async with new_session() as session:
        stmt = delete(TaskUserDB).where(TaskUserDB.user_id == user_id)
        try:
            await session.execute(stmt)
            await session.commit()
            return True
        except Exception as e:
            print(f"{e}")
            return False