from database.db import new_session
from sqlalchemy import select
from database.models import Task

# [Create] Create task
async def create_task(task_name: str):
    async with new_session as session:
        new_task = Task(name = task_name)
        session.add(new_task)
        await session.commit()

        return True

# [Read] Get all tasks
async def get_tasks():
    async with new_session as session:
        statement = select(Task)
        tasks = session.scalars(statement).all()
        print(tasks)

        return True

# [Update] Rename task
async def rename_task(task_id: int, new_name: str):
    async with new_session as session:
        task = await session.get(Task, task_id)

        if task:
            task.name = new_name

            await session.commit()
            return True

        else:
            print(f"Task #{task_id} not found")
            return False

# [Delete] Delete task
async def delete_task(task_id: int):
    async with new_session as session:
        task = await session.get(Task, task_id)

        if task:
            await session.delete(task)

            await session.commit()
            return True
        else:
            print(f"Task #{task_id} not found")
            return False