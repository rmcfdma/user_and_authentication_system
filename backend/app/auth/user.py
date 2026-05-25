"""
Sistema de autenticação e gerenciamento de usuários utilizando:

- FastAPI
- FastAPI Users
- JWT Authentication
- SQLAlchemy Async
- PostgreSQL (Supabase)

Responsabilidades deste módulo:

- Gerenciar conexão com banco
- Configurar autenticação JWT
- Gerenciar usuários
- Integrar FastAPI Users
- Validar usuários autenticados
- Enviar e-mails de verificação
"""

import uuid                                                            # Geração de identificadores UUID
from fastapi import Depends                                            # Sistema de dependências do FastAPI
from fastapi_users import FastAPIUsers                                 # Classe principal do FastAPI Users
from fastapi_users.authentication import (                             # Componentes de autenticação JWT
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy
)
from fastapi_users.db import SQLAlchemyUserDatabase                    # Integra FastAPI Users com SQLAlchemy
from fastapi_users.manager import BaseUserManager                      # Classe base do gerenciador de usuários
from sqlalchemy.ext.asyncio import AsyncSession                        # Sessões assíncronas do SQLAlchemy
from app.db import async_session_maker                                 # Factory de sessões do banco
from app.models.user import User                                       # Modelo SQLAlchemy do usuário
from app.schemas.user import (                                         # Schemas Pydantic de validação
    UserCreate,
    UserRead,
    UserUpdate
)
from app.config import settings                                        # Configurações globais da aplicação
from app.services.email import send_verify_email                       # Serviço de envio de e-mails


SECRET = settings.SECRET_KEY                                           # Chave secreta utilizada no JWT


# =========================================================
# DATABASE
# =========================================================

async def get_async_session():
    """Cria e fornece sessões assíncronas do banco."""
    async with async_session_maker() as session:                       # Abre sessão assíncrona
        yield session                                                  # Entrega sessão ao FastAPI

async def get_user_db(session: AsyncSession = Depends(get_async_session)): # Injeta sessão do banco
    """Integra o modelo User ao FastAPI Users."""
    yield SQLAlchemyUserDatabase(                                      # Cria adaptador SQLAlchemy
        session,
        User
    )


# =========================================================
# USER MANAGER
# =========================================================

class UserManager(BaseUserManager[User, uuid.UUID]):
    """Classe responsável pelas regras de negócio dos usuários."""
    reset_password_token_secret = SECRET                               # Chave do token reset password
    verification_token_secret = SECRET                                 # Chave do token verificação

    async def on_after_request_verify(self, user: User, token: str,  request=None,):
        """Evento executado após solicitar verificação de e-mail."""
        verify_url = (f"http://localhost:3000/verify?token={token}")   # URL enviada no e-mail
        await send_verify_email(user.email,verify_url)                 # Envia e-mail de verificação                               
        print("Email enviado com sucesso.")                            # Log simples no terminal


async def get_user_manager(user_db=Depends(get_user_db)):              # Injeta adaptador do usuário
    """Fornece o UserManager ao FastAPI Users."""
    yield UserManager(user_db)


# =========================================================
# JWT AUTHENTICATION
# =========================================================

bearer_transport = BearerTransport(                                    # Define transporte Bearer Token
    tokenUrl="auth/jwt/login"                                          # Endpoint responsável pelo login
)


def get_jwt_strategy():
    """Configura estratégia JWT."""
    return JWTStrategy(
        secret=SECRET,                                                 # Chave secreta do JWT
        lifetime_seconds=3600,                                         # Expiração do token (1h)
    )


auth_backend = AuthenticationBackend(
    name="jwt",                                                        # Nome interno do backend
    transport=bearer_transport,                                        # Transporte Bearer Token
    get_strategy=get_jwt_strategy,                                     # Estratégia de geração JWT
)


# =========================================================
# FASTAPI USERS
# =========================================================

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,                                                  # Gerenciador de usuários
    [auth_backend],                                                    # Backends de autenticação
)


current_active_user = fastapi_users.current_user(
    active=True                                                        # Permite apenas usuários ativos
)