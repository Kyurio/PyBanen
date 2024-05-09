from fastapi import APIRouter
from app.controller.postulaciones import PostPostulacion, GetPostulacion, PutPostulacion, DeletePostulacion, GetAllPostulacion
from app.schema.SchemaPostulacion import ResponsePostulacion
from typing import List

router = APIRouter()

@router.get("/GetAllPostulaciones/", response_model=List[ResponsePostulacion])
def listar_pustulacion_route():
    return GetAllPostulacion()

@router.get("/GetPostulacion/{id}", response_model=List[ResponsePostulacion])
def detalle_pustulacion_route(id: int):
    return GetPostulacion(id)

@router.post("/CreatePostulacion/")
def crear_postulacion_route(request: ResponsePostulacion):
    return PostPostulacion(request)

@router.put("/UpdatePostulacion/{id}")
def actualizar_postulacion_route(id: int, request: ResponsePostulacion):
    return PutPostulacion(id, request)
@router.delete("/DeletePostulacion/{id}")
def eliminar_postulacion_route(id: int):
    return DeletePostulacion(id)