from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UsuariosResponse(BaseModel):
    rut_post: str
    nom_post: str
    paterno: str
    materno: str
    nombre: str
    titulo: Optional[str]
    clave: str
    fecha_nac: Optional[datetime]
    tipo_doc: int
    log_licen: int
    log_movil: int
    fono1: str
    fono2: str
    direccion: str
    id_comuna: int
    id_region: int
    id_provincia: int
    email: str
    sbase: int
    liquido: int
    bruto: int
    estado: int

