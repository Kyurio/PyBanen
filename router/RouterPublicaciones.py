from fastapi import APIRouter
from app.controller.publicaciones import GetPublicaciones, GetPublicacionId
from app.schema.SchemaPublicaciones import ResponsePublicacion
from typing import List

router = APIRouter()

@router.get("/GetAllPublicaciones/", response_model=List[ResponsePublicacion])
def listar_publicaciones_route():
    return GetPublicaciones()

@router.get("/GetPublicacion/{id}", response_model=List[ResponsePublicacion])
def detalle_publicacion_route(id: int):
    return GetPublicacionId(id)

@router.post("/CreateUsuarios/")
def crear_publicacion_route(request: ResponsePublicacion):
    return PostUsuario(request)

@router.put("/UpdateUsuarios/")
def actualizar_publicacion_route(request: ResponsePublicacion):
    return UpdateUsuarios(request)

@router.delete("/DeleteUsuario/{usuario_id}")
def eliminar_publicaciono_route(id: int):
    return DeleteUsuario(id)