from database.db import new_session
from sqlalchemy import select
from database.models import TaskUser, User, Task

# [Create] Add user to task
async def add_user2task(user_id: int, task_id: int):
    async with new_session as session:
        new_user_task = TaskUser(user_id = user_id, task_id = task_id)
        session.add(new_user_task)
        await session.commit()

# [Read] Get users, where task == ...
async def get_users_by_task(task_id: int):
    async with new_session as session:
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
    async with new_session as session:
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
    async with new_session as session:
        task_user_list = session.get(TaskUser, task_id = task_id, user_id = user_id)

        if task_user_list:
            await session.delete(task_user_list)

            session.commit()
            return 0
        else:
            print("Something went wrong")
            return 0