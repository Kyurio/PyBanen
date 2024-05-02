from pydantic import BaseModel
from datetime import date, datetime
from decimal import Decimal

class ResponsePublicacion(BaseModel):
    bruto: int
    carga_hora: Decimal
    cod_cargo: str
    cod_city: str
    cod_oferta: str
    cod_pais: str
    cod_sucu: str
    cod_turno: str
    contrato: Decimal
    descripcion: str
    email_selec: str
    estado: Decimal
    estudios: Decimal
    experiencia: Decimal
    fecha: date
    fecha_hora: datetime
    fecha_ini: date
    fecha_pub: date
    fecha_ter: date
    graduado: Decimal
    ingles: Decimal
    licencia: str
    liquido: int
    log_discap: Decimal
    log_video: Decimal
    modalidad: Decimal
    nivel_lab: Decimal
    nom_oferta: str
    region: Decimal
    rut_empr: str
    sbase: int