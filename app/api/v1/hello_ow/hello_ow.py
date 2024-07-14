from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

router = APIRouter()


@router.get("/")
async def hello_mst(db: AsyncSession = Depends(get_db)):
    return {"message": f"Hello Microservice Template! db: {db}"}
