from sqlalchemy.ext.asyncio import AsyncSession # Async
from sqlalchemy import select # Async

from models import TestModel

async def get_data(db: AsyncSession):
    data = await db.execute(select(TestModel))
    result = data.scalars().fetchall()   # Load data from PG
    return result 
