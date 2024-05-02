from fastapi import APIRouter, HTTPException
from app.model.Publicaciones import Publicaciones
from app.schema.SchemaPublicaciones import ResponsePublicacion
from typing import List

router = APIRouter()


@router.get("/Publicaciones/", response_model=List[ResponsePublicacion])
async def obtener_paises():
    try:
        obj = Publicaciones()
        request = obj.get_all()
        return request

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
