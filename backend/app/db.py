from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    connect_args={
        "statement_cache_size": 0
    }
)

async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False
)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session