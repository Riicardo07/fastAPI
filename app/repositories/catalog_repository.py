from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.reflected import Carta, Categoria, Mesa, Presentacion

PRESENTACION_POR_FLAG = {
    "unidad": "Unidad",
    "tapa": "Tapa",
    "media": "Media Ración",
    "racion": "Ración",
}


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


def get_producto(db: Session, product_id: int):
    return db.get(Carta, product_id)


def list_presentaciones_producto(db: Session, producto):
    nombres = [nombre for flag, nombre in PRESENTACION_POR_FLAG.items() if getattr(producto, flag)]
    if not nombres:
        return []
    return db.scalars(select(Presentacion).where(Presentacion.nombre_presentacion.in_(nombres))).all()
