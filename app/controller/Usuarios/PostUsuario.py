from fastapi import APIRouter, HTTPException
from app.model.Usuario import Usuarios
from app.schema.SchemaUsuario import UsuariosResponse

router = APIRouter()

@router.post("/PostUsuario/")
def crear_usuario(request: UsuariosResponse):
    try:

        ususario_data = request.dict()
        response = Usuarios.create(ususario_data)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")