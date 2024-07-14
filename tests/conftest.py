import sys

import pytest_asyncio
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app import app


@pytest_asyncio.fixture(scope="module")
async def test_app():
    return app


@pytest_asyncio.fixture(scope="module")
async def test_client(test_app: FastAPI):
    """Create an HTTP client for testing"""
    async with AsyncClient(
        transport=ASGITransport(app=test_app), base_url="https://localhost:8000"
    ) as client:
        yield client


@pytest_asyncio.fixture(scope="module")
async def db_session():
    """Create 'an in-memory' SQLite database session."""
    async with create_async_engine("sqlite+aiosqlite:///:memory:") as engine:
        async_session = sessionmaker(bind=engine, class_=AsyncSession)
        async with async_session() as session:
            yield session
