from fastapi import APIRouter
from app.controller.Usuarios import GetUsuarios, PostUsuario, PutUsuario, DeleteUsuario
from app.schema.SchemaUsuario import UsuariosResponse
from typing import List

router = APIRouter()

@router.get("/GetAllUsuarios/", response_model=List[UsuariosResponse])
def listar_usuario_route():
    return GetUsuarios()

@router.post("/CreateUsuarios/")
def crear_usuario_route(request: UsuariosResponse):
    return PostUsuario(request)

@router.put("/UpdateUsuarios/{id}")
def actualizar_usuario_route(request: UsuariosResponse):
    return PutUsuario(request)

@router.delete("/DeleteUsuario/{usuario_id}")
def eliminar_usuario_route(id: int):
    return DeleteUsuario(id)