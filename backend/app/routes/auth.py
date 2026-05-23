from fastapi import APIRouter

from app.auth.user import auth_backend
from app.auth.user import fastapi_users

from app.schemas.user import UserCreate
from app.schemas.user import UserRead


router = APIRouter()

# POST   /auth/jwt/login                 -> Faz login e gera o token JWT do usuário
# POST   /auth/jwt/logout                -> Faz logout do usuário
# POST   /auth/register                  -> Cria um novo usuário
# POST   /auth/forgot-password           -> Envia/gera token para recuperação de senha
# POST   /auth/reset-password            -> Define uma nova senha usando o token de recuperação
# POST   /auth/request-verify-token      -> Gera token para verificação de email
# POST   /auth/verify                    -> Verifica/confirma o email do usuário


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate
    ),
    prefix="",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="",
    tags=["auth"],
)