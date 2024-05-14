from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schema.SchemaUsuario import UsuariosResponse


router = APIRouter()
@router.delete("/deletePostulacion/{id}")
def delete_publicacion(id: int):
    try:

        response = Usuarios.delete(id)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
