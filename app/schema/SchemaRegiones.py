from pydantic import BaseModel

class ResponseRegiones(BaseModel):
    id_region: int
    nom_region: str
    abreviatura: str
    capital: str