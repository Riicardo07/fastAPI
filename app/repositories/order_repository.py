from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.reflected import Carta, Mesa, Presentacion

NOMBRES_MESA_7 = ("Mesa 07", "Mesa 7")


def get_mesa_7(db: Session):
    return db.scalars(select(Mesa).where(Mesa.nombre_mesa.in_(NOMBRES_MESA_7))).first()


def get_producto(db: Session, product_id: int):
    return db.get(Carta, product_id)


def get_presentacion(db: Session, presentation_id: int):
    return db.get(Presentacion, presentation_id)


def create_order(db: Session, id_mesa: int, product_id: int, presentation_id: int):
    order = Order(id_mesa=id_mesa, id_producto_carta=product_id, id_presentacion=presentation_id)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def list_orders_mesa(db: Session, id_mesa: int):
    return db.scalars(select(Order).where(Order.id_mesa == id_mesa)).all()


def get_order(db: Session, order_id: int):
    return db.get(Order, order_id)


def delete_order(db: Session, order):
    db.delete(order)
    db.commit()
