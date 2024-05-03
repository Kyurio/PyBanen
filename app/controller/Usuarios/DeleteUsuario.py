from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios

router = APIRouter()

@router.delete("/DeleteUsuario/{rut}")
def delete_usuario(rut: str):
    try:
        print("rut a eliminar:", rut)
        response = Usuarios.delete(rut)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el usuario: {str(e)}")
