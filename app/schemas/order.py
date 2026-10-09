from pydantic import BaseModel, ConfigDict


class OrderCreate(BaseModel):
    table_id: int
    product_id: int
    presentation_id: int
    cantidad: int = 1


class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    table_id: int
    product_id: int
    presentation_id: int
