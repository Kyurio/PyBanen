from typing import List
from app.database.Database import Conexion
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class ResponsePais(BaseModel):
    id_pais: int
    nom_pais: str
    abreviatura: str

class Pais:

    db = Conexion()  # Instancia la clase MySQLConnection
    tabla = "paises"

    @staticmethod
    def create(quest: str) -> int:
        Pais.db.connect()  # Conecta a la base de datos
        try:
            query = f"INSERT INTO {Pais.tabla} (quest) VALUES ('{quest}')"
            Pais.db.execute(query)
            Pais.db.connection.commit()
            return Pais.db.connection
        finally:
            Pais.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def get(quest_id: int) -> dict:
        Pais.db.connect()  # Conecta a la base de datos
        try:
            query = f"SELECT * FROM {Pais.tabla} WHERE id = {quest_id}"
            result = Pais.db.execute(query)
            if result:
                return {"id_pais": result[0][0], "nom_pais": result[0][1], "abreviatura": result[0][2]}
            else:
                return None
        finally:
            Pais.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def update(quest_id: int, pregunta: str, respuesta: str) -> bool:
        Pais.db.connect()  # Conecta a la base de datos
        try:
            query = f"UPDATE {Pais.tabla} SET pregunta = '{pregunta}', respuesta = '{respuesta}' WHERE id = {quest_id}"
            Pais.db.execute(query)
            Pais.db.connection.commit()
            return True
        except:
            return False
        finally:
            Pais.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def delete(quest_id: int) -> bool:
        Pais.db.connect()  # Conecta a la base de datos
        try:
            query = f"DELETE FROM {Pais.tabla} WHERE id = {quest_id}"
            Pais.db.execute(query)
            Pais.db.connection.commit()
            return True
        except:
            return False
        finally:
            Pais.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def get_all() -> List[ResponsePais]:
        try:
            Pais.db.connect()  # Conecta a la base de datos
            query = f"SELECT * FROM {Pais.tabla}"
            result = Pais.db.execute(query)

            if not result:
                return []

            rows = [ResponsePais(id_pais=row[0], nom_pais=row[1], abreviatura=row[2]).dict() for row in result]
            return rows

        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
        finally:
            Pais.db.close()  # Cierra la conexión a la base de datos


