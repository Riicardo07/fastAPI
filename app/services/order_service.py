from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import order_repository as repo
from app.schemas.order import OrderCreate, OrderOut

MESA_PERMITIDA = 7
MENSAJE_MESA = "Operación permitida únicamente en la Mesa 7"


def _validar_mesa(table_id: int) -> None:
    if table_id != MESA_PERMITIDA:
        raise HTTPException(status_code=403, detail=MENSAJE_MESA)


def _mesa_7(db: Session):
    mesa = repo.get_mesa_7(db)
    if mesa is None:
        raise HTTPException(status_code=404, detail="La Mesa 7 no existe en el sistema")
    return mesa


def _to_order_out(order) -> OrderOut:
    return OrderOut(
        id=order.id,
        table_id=MESA_PERMITIDA,
        product_id=order.id_producto_carta,
        presentation_id=order.id_presentacion,
    )


def crear_pedido(db: Session, payload: OrderCreate) -> OrderOut:
    _validar_mesa(payload.table_id)
    if repo.get_producto(db, payload.product_id) is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    if repo.get_presentacion(db, payload.presentation_id) is None:
        raise HTTPException(status_code=404, detail="Presentación no encontrada")
    mesa = _mesa_7(db)
    order = repo.create_order(db, mesa.id, payload.product_id, payload.presentation_id)
    return _to_order_out(order)


def listar_pedidos(db: Session, table_id: int) -> list[OrderOut]:
    _validar_mesa(table_id)
    mesa = _mesa_7(db)
    return [_to_order_out(order) for order in repo.list_orders_mesa(db, mesa.id)]


def eliminar_pedido(db: Session, order_id: int) -> None:
    order = repo.get_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    mesa = _mesa_7(db)
    if order.id_mesa != mesa.id:
        raise HTTPException(status_code=403, detail=MENSAJE_MESA)
    repo.delete_order(db, order)
