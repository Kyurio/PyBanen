from fastapi import APIRouter, HTTPException
from app.model.Region import Regiones
from app.schema.SchemaRegiones import ResponseRegiones
from typing import List

router = APIRouter()

@router.get("/Regiones/", response_model=List[ResponseRegiones])
async def obtener_regiones():
    try:


        obj = Regiones()
        publicaciones = obj.get_all()
        return publicaciones

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

