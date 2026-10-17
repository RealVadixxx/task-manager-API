from database.db import new_session
from sqlalchemy import select
from database.models import User

# [Create] Create user
async def create_user(user_name: str):
    async with new_session as session:
        new_user = User(name = user_name)
        session.add(new_user)
        await session.commit()

# [Read] Get all users
async def get_users():
    async with new_session as session:
        statement = select(User)
        users = session.scalars(statement).all()
        print(users)

# [Update] Rename user
async def rename_user(user_id: int, new_name: str):
    async with new_session as session:
        user = await session.get(User, user_id)

        if user:
            user.name = new_name

            await session.commit()
            return 0

        else:
            print(f"User #{user_id} not found")
            return 1

# [Delete] Delete user
async def delete_user(user_id: int):
    async with new_session as session:
        user = await session.get(User, user_id)

        if user:
            await session.delete(user)

            await session.commit()
            return 0
        else:
            print(f"User #{user_id} not found")
            return 1