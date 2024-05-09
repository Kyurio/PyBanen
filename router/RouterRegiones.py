from fastapi import APIRouter
from app.controller.Regiones import GetRegiones
from app.schema.SchemaPublicaciones import ResponsePublicacion
from typing import List

router = APIRouter()

@router.get("/GetAllPublicaciones/", response_model=List[ResponsePublicacion])
def listar_regiones_route():
    return GetRegiones()

@router.post("/CreateUsuarios/")
def crear_regiones_route(request: ResponsePublicacion):
    return PostUsuario(request)

@router.put("/UpdateUsuarios/")
def actualizar_regiones_route(request: ResponsePublicacion):
    return UpdateUsuarios(request)

@router.delete("/DeleteUsuario/{usuario_id}")
def eliminar_regiones_route(id: int):
    return DeleteUsuario(id)