from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schema.SchemaUsuario import UsuariosResponse

router = APIRouter()
@router.get("/GetPostulacion/")
def listar_postulaciones():
    try:

        response = Usuarios.get_all()
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
