from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories import catalog_repository as repo
from app.schemas.catalog import CategoryOut, PresentationOut, ProductOut, TableOut

router = APIRouter(tags=["catalog"])


@router.get("/tables", response_model=list[TableOut])
def get_tables(db: Session = Depends(get_db)):
    return repo.list_mesas(db)


@router.get("/categories", response_model=list[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return repo.list_categorias(db)


@router.get("/categories/{category_id}/products", response_model=list[ProductOut])
def get_category_products(category_id: int, db: Session = Depends(get_db)):
    if repo.get_categoria(db, category_id) is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return repo.list_productos(db, category_id)


@router.get("/presentations", response_model=list[PresentationOut])
def get_presentations(db: Session = Depends(get_db)):
    return repo.list_presentaciones(db)
