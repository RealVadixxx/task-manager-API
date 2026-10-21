from ui.api.task_user import add_user2task as add_my_user
from ui.api.task_user import get_tasks_by_user as get_my_tasks_by_user
from ui.api.task_user import get_users_by_task as get_my_users_by_task
from ui.api.task_user import remove_user2task as remove_my_user


def get_users_by_task(task_id: int):
    return get_my_users_by_task(task_id)

def get_tasks_by_user(user_id: int):
    return get_my_tasks_by_user(user_id)

def add_user(user_id: int, task_id: int):
    return add_my_user(user_id, task_id)

def remove_user(user_id: int, task_id: int):
    remove_my_user(user_id, task_id)
