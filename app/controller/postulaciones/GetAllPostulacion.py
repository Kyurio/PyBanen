from fastapi import APIRouter, HTTPException
from app.model.Postulacion import Postulacion

router = APIRouter()
@router.get("/GetPostulacion/")
def listar_postulaciones():
    try:

        response = Postulacion.get_all()
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil: {str(e)}")
