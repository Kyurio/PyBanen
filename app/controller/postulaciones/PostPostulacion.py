from fastapi import APIRouter, HTTPException
from app.model.Postulacion import Postulacion
from app.schema.SchemaPostulacion import ResponsePostulacion

router = APIRouter()
@router.post("/PostPostulacion/")
def crear_postulacion(request: ResponsePostulacion):
    try:

        print(request)

        response = Postulacion.create(request.cod_oferta, request.rut_post)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
