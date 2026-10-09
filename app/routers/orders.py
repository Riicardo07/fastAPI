from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.order import OrderCreate, OrderOut
from app.services import order_service

router = APIRouter(tags=["orders"])


@router.post("/orders", response_model=OrderOut, status_code=201)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    return order_service.crear_pedido(db, payload)


@router.get("/tables/{table_id}/orders", response_model=list[OrderOut])
def get_table_orders(table_id: int, db: Session = Depends(get_db)):
    return order_service.listar_pedidos(db, table_id)


@router.delete("/orders/{order_id}", status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order_service.eliminar_pedido(db, order_id)
    return None
