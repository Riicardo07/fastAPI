from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories import order_repository as repo
from app.schemas.order import OrderCreate, OrderOut

router = APIRouter(tags=["orders"])

MESA_PERMITIDA = 7
MENSAJE_MESA = "Operación permitida únicamente en la Mesa 7"


def to_order_out(order) -> OrderOut:
    return OrderOut(
        id=order.id,
        table_id=MESA_PERMITIDA,
        product_id=order.id_producto_carta,
        presentation_id=order.id_presentacion,
    )


@router.post("/orders", response_model=OrderOut, status_code=201)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    if payload.table_id != MESA_PERMITIDA:
        raise HTTPException(status_code=403, detail=MENSAJE_MESA)
    if repo.get_producto(db, payload.product_id) is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    if repo.get_presentacion(db, payload.presentation_id) is None:
        raise HTTPException(status_code=404, detail="Presentación no encontrada")
    mesa = repo.get_mesa_7(db)
    if mesa is None:
        raise HTTPException(status_code=404, detail="La Mesa 7 no existe en el sistema")
    order = repo.create_order(db, mesa.id, payload.product_id, payload.presentation_id)
    return to_order_out(order)


@router.get("/tables/{table_id}/orders", response_model=list[OrderOut])
def get_table_orders(table_id: int, db: Session = Depends(get_db)):
    if table_id != MESA_PERMITIDA:
        raise HTTPException(status_code=403, detail=MENSAJE_MESA)
    mesa = repo.get_mesa_7(db)
    if mesa is None:
        raise HTTPException(status_code=404, detail="La Mesa 7 no existe en el sistema")
    return [to_order_out(order) for order in repo.list_orders_mesa(db, mesa.id)]


@router.delete("/orders/{order_id}", status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = repo.get_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    mesa = repo.get_mesa_7(db)
    if mesa is None or order.id_mesa != mesa.id:
        raise HTTPException(status_code=403, detail=MENSAJE_MESA)
    repo.delete_order(db, order)
    return None
