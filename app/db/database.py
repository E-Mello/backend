from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

# URL for the PostgreSQL database (make sure it's correct)
url_database = "postgresql+asyncpg://neondb_owner:JaZ56ApvftiW@ep-shrill-shape-a53dkotf.us-east-2.aws.neon.tech/neondb"

# Create an async engine using the correct driver
engine: AsyncEngine = create_async_engine(url_database)

# Create an AsyncSession sessionmaker for async operations
SessionLocal = sessionmaker(
    bind=engine,  # Corrige o parâmetro `bind`
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False  # Esse parâmetro é desnecessário, remova se persistir o erro
)


# Dependency that handles DB sessions
async def get_db():
    async with SessionLocal() as db:
        yield db
