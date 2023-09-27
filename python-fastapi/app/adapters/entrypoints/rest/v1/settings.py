from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from app.configs.settins import DBSettings, get_db_settings

router = APIRouter(prefix="/v1")


@router.get("/settings")
async def read_settings(
    settings: Annotated[DBSettings, Depends(get_db_settings)]
):
    return {"db_name": settings.db_dsn}
