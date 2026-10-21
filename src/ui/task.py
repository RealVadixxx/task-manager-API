from ui.api.task import create_task as create_my_task
from ui.api.task import delete_task as delete_my_task
from ui.api.task import get_tasks as get_my_tasks
from ui.api.task import get_task as get_my_task
from ui.api.task import rename_task as rename_my_task
from ui.task_user import get_tasks_by_user, get_users_by_task
from ui.user import get_users as get_my_users
from ui.task_user import remove_user as remove_my_user
from ui.task_user import add_user as add_my_user

# Create
def create_task():
    task_name = input("Enter task name: ")
    return create_my_task(task_name)

# Read
def get_tasks():
    print(get_my_tasks())

    print()
    task_id = input("Select task to edit: ")
    manage_task(task_id)

def get_task_info(task_id: int):
    print(get_my_task(task_id))
    print(get_users_by_task(task_id))

# Update
def manage_task(task_id: int):
    get_task_info(task_id)
    print("-" * 10)
    print("1. Rename")
    print("2. Add user")
    print("3. Remove user")
    print("4. Delete task")
    print("0. Exit")
    print(" ")
    choice = input("Enter: ")
    match (choice):
        case 1: rename_task(task_id)
        case 2: add_user(task_id)
        case 3: remove_user(task_id)
        case 4: delete_task(task_id)
        case 0: get_tasks()
        case _: get_tasks()

def rename_task(task_id: int):
    print("-" * 10)

    task_name = input("Enter new task name:")
    return rename_my_task(task_id, task_name)

def add_user(task_id):
    print(get_my_users)
    print("-" * 10)
    user_id = input("Enter user_id: ")
    return add_my_user(user_id, task_id)

def remove_user(task_id: int):
    print(get_my_users)
    print("-" * 10)
    user_id = input("Enter user_id: ")
    return remove_my_user(user_id, task_id)

def delete_task(task_id: int):
    return delete_my_task(task_id)
