from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schema.SchemaUsuario import UsuariosResponse

router = APIRouter()
@router.get("/GetPostulacion/{id}")
def detalle_postulaciones(id: int):
    try:

        response = Usuarios.get(id)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
