from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ResponsePostulacion(BaseModel):
    cod_oferta: str
    rut_post: str


class ResponseGetPostulacion(BaseModel):
    id_postulacion: int
    cod_oferta: str
    rut_post: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
