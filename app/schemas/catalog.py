from pydantic import BaseModel, ConfigDict


class CategoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre_categoria: str


class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    id_categoria: int
    producto: str
    unidad: int
    tapa: int
    media: int
    racion: int


class PresentationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre_presentacion: str


class TableOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre_mesa: str
