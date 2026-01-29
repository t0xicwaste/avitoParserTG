import os

from db.base import Base
from dotenv import load_dotenv
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine,

load_dotenv()

url = URL.create(
    "postgresql+asyncpg",
    username=os.environ.get("USERNAME"),
    password=os.environ.get("PASSWORD"),
    host=os.environ.get("HOST"),
    port=5432,
    database=os.environ.get("DATABASE"),
)


engine = create_async_engine(url, echo=True)
session_factory = async_sessionmaker(bind=engine, class_=AsyncSession)


async def flush_db(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    return session_factory()
