from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

if settings.DATABASE_URL:
    engine = create_async_engine(settings.DATABASE_URL, echo=True)
else:
    raise ValueError("DATABASE_URL is not configured or is set to None.")


async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session
