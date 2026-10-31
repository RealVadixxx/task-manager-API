import logging
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy import select

from database.db import new_session
from database.models import UserDB
from schemas.user import UserSchema


logger = logging.getLogger("task_manager")

# [Create] Create user
async def create_user(user: UserSchema) -> bool:
    async with new_session() as session:
        try:
            new_user = UserDB(name = user.name)
            session.add(new_user)

            await session.commit()
            logger.info(f"DB | Create user | user_name: {user.name}")
            return True
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False

# [Read] Get all users
async def get_users() -> list[UserSchema] | None:
    async with new_session() as session:
        try:
            users = await session.scalars(select(UserDB))
            users = users.all()

            result = [UserSchema(id = user.id, name = user.name) for user in users]
            logger.info(f"DB | Get users")
            return result
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return None
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return None

async def get_user(user_id) -> UserSchema | None:
    async with new_session() as session:
        try:
            user = await session.get(UserDB, user_id)
            if user:
                logger.info(f"DB | Get user | uid: {user_id}")
                return UserSchema(id = user.id, name = user.name)
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False
        
# [Update] Rename user
async def rename_user(user_id: int, new_name: str) -> bool:
    async with new_session() as session:
        try:
            user = await session.get(UserDB, user_id)
            old_name = user.name
            if user:
                user.name = new_name

                await session.commit()
                logger.info(f"DB | Rename user | uid: {user_id} | Name: {old_name} -> {user.name}")
                return True

            else:
                print(f"User #{user_id} not found")
                return False
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False

# [Delete] Delete user
async def delete_user(user_id: int) -> bool:
    async with new_session() as session:
        try:
            user = await session.get(UserDB, user_id)
    
            if user:
                await session.delete(user)
    
                await session.commit()
                logger.info(f"DB | Delete user | uid: {user_id}")
                return True
    
            else:
                print(f"User #{user_id} not found")
                return False
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Ошибка целостности БД | {e}")
            return False
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД | {e}")
            return False