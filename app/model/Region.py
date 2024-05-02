from typing import List
from app.database.Database import Conexion
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class ResponseReguiones(BaseModel):
    id_region: int
    nom_region: str
    abreviatura: str
    capital: str

class Regiones:

    db = Conexion()
    tabla = "regiones"

    @staticmethod
    def create(quest: str) -> int:
        Regiones.db.connect()  # Conecta a la base de datos
        try:
            query = f"INSERT INTO {Regiones.tabla} (quest) VALUES ('{quest}')"
            Regiones.db.execute(query)
            Regiones.db.connection.commit()
            return Regiones.db.connection
        finally:
            Regiones.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def get(quest_id: int) -> dict:
        Regiones.db.connect()  # Conecta a la base de datos
        try:
            query = f"SELECT * FROM {Regiones.tabla} WHERE id = {quest_id}"
            result = Regiones.db.execute(query)
            if result:
                return {"id_Regiones": result[0][0], "nom_Regiones": result[0][1], "abreviatura": result[0][2]}
            else:
                return None
        finally:
            Regiones.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def update(quest_id: int, pregunta: str, respuesta: str) -> bool:
        Regiones.db.connect()  # Conecta a la base de datos
        try:
            query = f"UPDATE {Regiones.tabla} SET pregunta = '{pregunta}', respuesta = '{respuesta}' WHERE id = {quest_id}"
            Regiones.db.execute(query)
            Regiones.db.connection.commit()
            return True
        except:
            return False
        finally:
            Regiones.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def delete(quest_id: int) -> bool:
        Regiones.db.connect()  # Conecta a la base de datos
        try:
            query = f"DELETE FROM {Regiones.tabla} WHERE id = {quest_id}"
            Regiones.db.execute(query)
            Regiones.db.connection.commit()
            return True
        except:
            return False
        finally:
            Regiones.db.close()  # Cierra la conexión a la base de datos
    @staticmethod
    def get_all() -> List[ResponseReguiones]:
        try:
            Regiones.db.connect()
            query = f"SELECT * FROM {Regiones.tabla}"
            result = Regiones.db.execute(query)

            if not result:
                return []

            rows = [ResponseReguiones(id_region=row[0], nom_region=row[1], abreviatura=row[2], capital=row[3]).dict() for row in result]
            return rows

        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
        finally:
            Regiones.db.close()  # Cierra la conexión a la base de datos





