from database.db import new_session
from sqlalchemy import select
from database.models import TaskDB
from schemas.task import TaskSchema
from database.exceptions import DBError

# [Create] Create task
async def create_task(task: TaskSchema) -> bool:
    async with new_session() as session:
        try:
            session.add(TaskDB(name = task.name))
            await session.commit()

            return True
        except Exception as e:
            print(e)
            return False

# [Read] Get all tasks
async def get_tasks() -> list | None:
    async with new_session() as session:
        try:
            tasks = await session.scalars(select(TaskDB))
            tasks = tasks.all()
            result = [TaskSchema(id = task.id, name = task.name).model_dump() for task in tasks]
            if result == [] or result:
                return result
        except Exception as e:
            print(e)
            return None

async def get_task(task_id) -> TaskSchema | None:
    async with new_session() as session:
        try:
            task = await session.get(TaskDB, task_id)
            if task:
                return TaskSchema(id = task.id, name = task.name)
            else:
                raise DBError("get_task")
        except Exception as e:
            print(e)
            return None
        

# [Update] Rename task
async def rename_task(task_id: int, new_name: str) -> bool:
    async with new_session() as session:
        try:
            task = await session.get(TaskDB, task_id)

            if task:
                task.name = new_name

                await session.commit()

                return True

            else:
                print(f"Task #{task_id} not found")
                return False
        except Exception as e:
            print(e)
            return False

# [Delete] Delete task
async def delete_task(task_id: int) -> bool:
    async with new_session() as session:
        try:
            task = await session.get(TaskDB, task_id)

            if task:
                await session.delete(task)

                await session.commit()

                return True
            else:
                print(f"Task #{task_id} not found")
                return False
        except Exception as e:
            print(e)
            return False