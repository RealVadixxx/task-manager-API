from database.db import new_session
from sqlalchemy import select, delete
from database.models import TaskUser, User, Task

# [Create] Add user to task
async def add_user2task(user_id: int, task_id: int):
    async with new_session() as session:
        new_user_task = TaskUser(user_id = user_id, task_id = task_id)
        session.add(new_user_task)
        await session.commit()

        links = await session.scalars(select(TaskUser))
        links = links.all()
        result = [{"user.id": link.user_id, "name": link.task_id} for link in links]

        return result

# [Read] Get users, where task == ...
async def get_users_by_task(task_id: int):
    async with new_session() as session:
        query = (
            select(User)
            .join(TaskUser, User.id == TaskUser.user_id)
            .where(TaskUser.task_id == task_id)
        )
        query_result = await session.execute(query)
        result = query_result.scalars().all()

        return result

# [Read] Get tasks, where user == ...
async def get_tasks_by_user(user_id: int):
    async with new_session() as session:
        query = (
            select(Task)
            .join(TaskUser, Task.id == TaskUser.task_id)
            .where(TaskUser.user_id == user_id)
        )
        query_result = await session.execute(query)
        result = query_result.scalars().all()

        return result

# [Delete] Remove user in task
async def remove_user_in_task(user_id: int, task_id: int):
    async with new_session() as session:
        task_user_list = session.get(TaskUser, task_id = task_id, user_id = user_id)

        if task_user_list:
            await session.delete(task_user_list)

            session.commit()

            links = await session.scalars(select(TaskUser))
            links = links.all()
            result = [{"user.id": link.user_id, "name": link.task_id} for link in links]

            return result
        else:
            print("Something went wrong")
            return None

# [Delete] Delete task
async def delete_task(task_id: int):
    async with new_session() as session:
        stmt = delete(TaskUser).where(TaskUser.task_id == task_id)
        try:
            await session.execute(stmt)
            session.commit()
            return True
        except Exception as e:
            print(f"{e}")
            return False

# [Delete] Remove user
async def delete_user(user_id: int):
    async with new_session() as session:
        stmt = delete(TaskUser).where(TaskUser.user_id == user_id)
        try:
            await session.execute(stmt)
            session.commit()
            return True
        except Exception as e:
            print(f"{e}")
            return False