from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios

router = APIRouter()

@router.put("/PutUsuario/{rut}")
def update_usuario(rut: str):
    try:
        response = Usuarios.delete(rut)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {str(e)}")
