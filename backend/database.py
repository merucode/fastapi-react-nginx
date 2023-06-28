import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine # Async
from sqlalchemy.orm import declarative_base            

db_host = os.environ["INSTANCE_HOST"]  # Read ENV file in Docker compose
db_user = os.environ["DB_USER"]  
db_pass = os.environ["DB_PASS"]
db_name = os.environ["DB_NAME"] 
db_port = os.environ["DB_PORT"]

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}" # Async
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True) # Async
Base = declarative_base()

# Async
async def get_async_db() -> AsyncSession:
    db= AsyncSession(bind=engine)
    try:
        yield db
    finally:
        await db.close()
