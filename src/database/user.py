from database.db import new_session
from sqlalchemy import select
from database.models import UserDB
from schemas.user import UserSchema

# [Create] Create user
async def create_user(user: UserSchema) -> bool:
    async with new_session() as session:
        try:
            new_user = UserDB(name = user.name)
            session.add(new_user)

            await session.commit()

            return True
        except Exception as e:
            print(e)
            return False

# [Read] Get all users
async def get_users() -> list[UserSchema] | None:
    async with new_session() as session:
        try:
            users = await session.scalars(select(UserDB))
            users = users.all()

            result = [UserSchema(id = user.id, name = user.name) for user in users]
            
            return result
        except Exception as e:
            print(e)
            return None

async def get_user(user_id) -> UserSchema | None:
    async with new_session() as session:
        try:
            user = await session.get(UserDB, user_id)
            if user:
                return UserSchema(id = user.id, name = user.name)
        except Exception as e:
            print(e)
            return None
        
# [Update] Rename user
async def rename_user(user_id: int, new_name: str) -> bool:
    async with new_session() as session:
        try:
            user = await session.get(UserDB, user_id)

            if user:
                user.name = new_name

                await session.commit()

                return True

            else:
                print(f"User #{user_id} not found")
                return False
        except Exception as e:
            print(e)
            return False

# [Delete] Delete user
async def delete_user(user_id: int) -> bool:
    async with new_session() as session:
        try:
            user = await session.get(UserDB, user_id)
    
            if user:
                await session.delete(user)
    
                await session.commit()
                
                return True
    
            else:
                print(f"User #{user_id} not found")
                return False
        except Exception as e:
            print(e)
            return False