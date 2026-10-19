from ui.api.task import (
    create_task as create_my_task, 
    get_tasks as get_my_tasks,
    rename_task as rename_my_task,
    delete_task as delete_my_task
    )
from ui.task_user import get_users_by_task, get_tasks_by_user


def create_task():
    task_name = input("Enter task name: ")
    return create_my_task(task_name)

def get_tasks():
    print(get_my_tasks())

    print()
    task_id = input("Select task to edit: ")
    manage_task(choice)

def get_task_info(task_id: int):
    
    get_users_by_task(task_id)

def manage_task(task_id: int):
    get_task_info(task_id)



def rename_task():
    get_tasks()
    print("-" * 10)

    task_name = input("Enter new task name:")


