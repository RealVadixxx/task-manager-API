from ui.api.task import get_tasks as get_my_tasks
from ui.api.task_user import add_user2task as add_my_user
from ui.api.task_user import get_tasks_by_user
from ui.api.task_user import remove_user2task as remove_my_user
from ui.api.user import create_user as create_my_user
from ui.api.user import delete_user as delete_my_user
from ui.api.user import get_user as get_my_user
from ui.api.user import get_users as get_my_users
from ui.api.user import rename_user as rename_my_user


# Create
def create_user():
    user_name = input("Enter user name: ")
    return create_my_user(user_name)

# Read
def get_users():
    print(get_my_users())

    print()
    user_id = input("Select user to edit: ")
    manage_user(user_id)

def get_user_info(user_id: int):
    print(get_my_user(user_id))
    print(get_tasks_by_user(user_id))

# Update
def manage_user(user_id: int):
    get_user_info(user_id)
    print("-" * 10)
    print("1. Rename")
    print("2. Add task")
    print("3. Remove task")
    print("4. Delete user")
    print("0. Exit")
    print(" ")
    choice = input("Enter: ")
    match (choice):
        case 1: rename_user(user_id)
        case 2: add_task(user_id)
        case 3: remove_task(user_id)
        case 4: delete_user(user_id)
        case 0: get_users()
        case _: get_users()

def rename_user(user_id: int):
    print("-" * 10)

    user_name = input("Enter new user name:")
    return rename_my_user(user_name)

def add_task(user_id: int):
    print(get_my_tasks())
    print("-" * 10)
    task_id = input("Enter task_id: ")
    return add_my_user(user_id, task_id)

def remove_task(user_id: int):
    print(get_my_tasks())
    print("-" * 10)
    task_id = input("Enter task_id: ")
    return remove_my_user(user_id, task_id)

def delete_user(user_id: int):
    return delete_my_user(user_id)
