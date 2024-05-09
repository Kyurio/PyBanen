from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schema.SchemaUsuario import UsuariosResponse

router = APIRouter()
@router.put("/PutPostulacion/{id}")
def actualiza_publicacion(id: int, request: UsuariosResponse):
    try:
        data = request.dict()
        response = Usuarios.update(id, data)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
