from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schema.SchemaUsuario import UsuariosResponse
from typing import List
router = APIRouter()

@router.get("/Usuarios/", response_model=List[UsuariosResponse])
async def obtener_paises():
    try:
        obj = Usuarios()
        paises = obj.get_all()
        return paises

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
