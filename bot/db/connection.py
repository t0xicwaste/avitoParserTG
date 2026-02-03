from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import URL

from db.base import Base

import os
from dotenv import load_dotenv

load_dotenv()

url = URL.create(
    'postgresql+asyncpg',
    username = os.getenv('USERNAME'),
    password = os.getenv('PASSWORD'),
    host = os.getenv('HOST'),
    port = int(os.getenv('PORT', "5432")),
    database = os.getenv('DATABASE')
)

engine = create_async_engine(url, echo=True)
session_factory = async_sessionmaker(bind=engine, class_=AsyncSession)

async def flush_db(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def get_session():
    return session_factory()
