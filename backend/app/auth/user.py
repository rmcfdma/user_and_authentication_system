import uuid
from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (AuthenticationBackend, BearerTransport, JWTStrategy)
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.manager import BaseUserManager
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_session_maker
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.config import settings
from app.services.email import send_verify_email


SECRET = settings.SECRET_KEY

# =========================
# DATABASE
# =========================

async def get_async_session():
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


# =========================
# USER MANAGER
# =========================

class UserManager(BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request=None,
    ):
        verify_url = f"http://localhost:3000/verify?token={token}"

        await send_verify_email(
            user.email,
            verify_url
        )
        print("Email enviado com sucesso.")
        


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


# =========================
# JWT
# =========================

bearer_transport = BearerTransport(
    tokenUrl="auth/jwt/login"
)


def get_jwt_strategy():
    return JWTStrategy(
        secret=SECRET,
        lifetime_seconds=3600,
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


# =========================
# FASTAPI USERS
# =========================

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


current_active_user = fastapi_users.current_user(active=True)