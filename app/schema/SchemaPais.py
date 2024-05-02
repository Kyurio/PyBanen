from pydantic import BaseModel

class PaisResponse(BaseModel):
    id_pais: int
    nom_pais: str
    abreviatura: str