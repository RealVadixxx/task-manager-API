from database.db import new_session
from sqlalchemy import select
from database.models import TaskDB
from schemas.task import TaskSchema

# [Create] Create task
async def create_task(task: TaskSchema) -> list | None:
    async with new_session() as session:
        try:
            session.add(TaskDB(name = task.name))
            await session.commit()

            tasks = await session.scalars(select(TaskDB))
            tasks = tasks.all()
            result = [{"id": task.id, "name": task.name} for task in tasks]

            return result
        except Exception as e:
            print(f"Something went wrong: {e}")
            return None

# [Read] Get all tasks
async def get_tasks() -> list:
    async with new_session() as session:
        tasks = await session.scalars(select(TaskDB))
        tasks = tasks.all()
        result = [{"id": task.id, "name": task.name} for task in tasks]

        return result

async def get_task(task_id):
    async with new_session() as session:
        task = await session.get(TaskDB, task_id)
        if task:
            return {"task_id": task.id, "task_name": task.name}
        

# [Update] Rename task
async def rename_task(task_id: int, new_name: str) -> list | None:
    async with new_session() as session:
        task = await session.get(TaskSchema, task_id)

        if task:
            task.name = new_name

            await session.commit()
            tasks = await session.scalars(select(TaskDB))
            tasks = tasks.all()
            result = [{"id": task.id, "name": task.name} for task in tasks]

            return result

        else:
            print(f"Task #{task_id} not found")
            return None

# [Delete] Delete task
async def delete_task(task_id: int) -> list | None:
    async with new_session() as session:
        task = await session.get(TaskSchema, task_id)

        if task:
            await session.delete(task)

            await session.commit()

            tasks = await session.scalars(select(TaskDB))
            tasks = tasks.all()
            result = [{"id": task.id, "name": task.name} for task in tasks]

            return result
        else:
            print(f"Task #{task_id} not found")
            return None