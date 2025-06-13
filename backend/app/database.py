import os
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql+asyncpg://neondb_owner:npg_kZy6UBruXfV1@ep-broad-sky-a5aydyf7-pooler.us-east-2.aws.neon.tech/neondb"
engine = create_async_engine(DATABASE_URL, echo=True)
session = AsyncSession(engine)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)