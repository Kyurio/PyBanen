from fastapi import APIRouter, HTTPException
from app.model.Pais import Pais  # Importa la clase Pais
from typing import List

router = APIRouter()

@router.get("/paises/", response_model=List[PaisResponse])
async def obtener_paises():
    try:
        obj = Pais()
        paises = obj.get_all()
        print("respuesta del controlador:", paises)
        return paises

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
