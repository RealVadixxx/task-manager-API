from fastapi import APIRouter, status

from database.task_user import (
    add_user2task as add_my_user2task,
    remove_user_in_task as remove_my_user_in_task,
    get_tasks_by_user as get_my_tasks_by_user,
    get_users_by_task as get_my_users_by_task
)

router = APIRouter()


# Create
@router.patch("/tasks/edit/users/add")
async def add_user2task(user_id: int, task_id: int):
    try:
        task = await (add_my_user2task(user_id, task_id))
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Read
@router.get("/tasks/users")
async def get_users_by_task(task_id: int):
    """ Get users by task """
    try:
        task = await get_my_users_by_task(task_id)
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Read
@router.get("/users/tasks")
async def get_tasks_by_user(user_id: int):
    try:
        task = await get_my_tasks_by_user(user_id)
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

# Update / Delete
@router.patch("/tasks/edit/users/remove")
async def remove_user2task(user_id: int, task_id: int):
    try:
        task = await (remove_my_user_in_task(user_id, task_id))
        if task:
            return task
    except Exception as e:
        print(f"Something went wrong: {e}")
        return status.HTTP_500_INTERNAL_SERVER_ERROR

