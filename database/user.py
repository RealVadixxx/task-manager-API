from database.db import new_session
from sqlalchemy import select
from database.models import User

# [Create] Create user
async def create_user(user_name: str) -> list | None:
    async with new_session() as session:
        try:
            new_user = User(name = user_name)
            session.add(new_user)

            await session.commit()

            users = await session.scalars(select(User))
            users = users.all()
            result = [{"id": user.id, "name": user.name} for user in users]

            return result
        except Exception as e:
            print(f"Something went wrong: {e}")
            return None

# [Read] Get all users
async def get_users() -> list:
    async with new_session() as session:
        users = await session.scalars(select(User))
        users = users.all()

        result = [{"id": user.id, "name": user.name} for user in users]
        return result

# [Update] Rename user
async def rename_user(user_id: int, new_name: str) -> list | None:
    async with new_session() as session:
        user = await session.get(User, user_id)

        if user:
            user.name = new_name

            await session.commit()

            users = await session.scalars(select(User))
            users = users.all()
            result = [{"id": user.id, "name": user.name} for user in users]

            return result

        else:
            print(f"User #{user_id} not found")
            return None

# [Delete] Delete user
async def delete_user(user_id: int) -> list | None:
    async with new_session() as session:
        user = await session.get(User, user_id)

        if user:
            await session.delete(user)

            await session.commit()
            users = await session.scalars(select(User))
            users = users.all()
            result = [{"id": user.id, "name": user.name} for user in users]

            return result

        else:
            print(f"User #{user_id} not found")
            return None