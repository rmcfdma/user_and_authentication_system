from fastapi import HTTPException
from sqlalchemy import select
from app.models.user import User
from app.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi import APIRouter
from app.auth.user import fastapi_users
from app.schemas.user import UserRead
from app.schemas.user import UserUpdate
from app.auth.user import current_active_user

router = APIRouter()

# GET    /users/me        -> Retorna os dados do usuário autenticado
# PATCH  /users/me        -> Atualiza os dados do usuário autenticado
# GET    /users/{id}      -> Busca um usuário pelo ID
# PATCH  /users/{id}      -> Atualiza um usuário pelo ID
# DELETE /users/{id}      -> Remove um usuário pelo ID

router.include_router(
    fastapi_users.get_users_router(
        UserRead,
        UserUpdate
    ),
    prefix="",
    tags=["users"],
)

@router.get("/me")
async def me(user=Depends(current_active_user)):
    return user

@router.get("/by-email/{email}")
async def get_user_by_email(
    email: str,
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(
        select(User).where(User.email == email)
    )

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return user

@router.delete("/by-email/{email}")
async def delete_user_by_email(
    email: str,
    session: AsyncSession = Depends(get_async_session)
):
    query = select(User).where(User.email == email)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )
    await session.delete(user)
    await session.commit()
    return {
        "message": "Usuário deletado"
        }