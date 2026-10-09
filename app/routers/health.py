from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["core"])


@router.get("/")
def read_root() -> dict:
    return {
        "message": "Restaurant API operativa",
        "docs": "/docs",
    }


@router.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "Restaurant API",
        "assigned_tables": settings.allowed_tables_list,
    }
