import asyncio

from app.db import engine
from app.models.base import Base

# IMPORTANTE:
# importa o model User para o SQLAlchemy registrar a tabela
from app.models.user import User


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(create_db())