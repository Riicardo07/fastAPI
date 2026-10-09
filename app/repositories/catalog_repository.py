from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.reflected import Carta, Categoria, Mesa, Presentacion


def list_mesas(db: Session):
    return db.scalars(select(Mesa)).all()


def list_categorias(db: Session):
    return db.scalars(select(Categoria)).all()


def get_categoria(db: Session, categoria_id: int):
    return db.get(Categoria, categoria_id)


def list_productos(db: Session, categoria_id: int):
    return db.scalars(select(Carta).where(Carta.id_categoria == categoria_id)).all()


def list_presentaciones(db: Session):
    return db.scalars(select(Presentacion)).all()
