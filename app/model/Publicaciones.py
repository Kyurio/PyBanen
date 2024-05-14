from typing import List
from app.database.Database import Conexion
from app.schema.SchemaPublicaciones import ResponsePublicacion

class Publicaciones:

    db = Conexion()  # Instancia la clase MySQLConnection
    tabla = "reclu100"

    @staticmethod
    def create(quest: str) -> int:
        Publicaciones.db.connect()  # Conecta a la base de datos
        try:
            query = f"INSERT INTO {Publicaciones.tabla} (quest) VALUES ('{quest}')"
            Publicaciones.db.execute(query)
            Publicaciones.db.connection.commit()
            return Publicaciones.db.connection
        finally:
            Publicaciones.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def get(id: str) -> dict:
        Publicaciones.db.connect()
        try:
            query = f"SELECT * FROM {Publicaciones.tabla} WHERE cod_oferta = '{id}'"

            result = Publicaciones.db.execute(query)

            if not result:
                return []

            rows = [ResponsePublicacion(
                cod_oferta=row[0],
                nom_oferta=row[1],
                rut_empr=row[2],
                cod_pais=row[3],
                cod_city=row[4],
                cod_cargo=row[5],
                cod_sucu=row[6],
                cod_turno=row[7],
                fecha=row[8],
                fecha_pub=row[9],
                fecha_ini=row[10],
                fecha_ter=row[11],
                sbase=row[12],
                liquido=row[13],
                bruto=row[14],
                contrato=row[15],
                carga_hora=row[16],
                nivel_lab=row[17],
                log_video=row[18],
                estado=row[19],
                fecha_hora=row[20],
                modalidad=row[21],
                ingles=row[22],
                estudios=row[23],
                licencia=row[24],
                region=row[25],
                titulo=row[26],
                experiencia=row[27],
                log_discap=row[28],
                graduado=row[29],
                descripcion=row[30],
                email_selec=row[31]
            ).dict() for row in result]

            return rows

        finally:
            Publicaciones.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def update(quest_id: int, pregunta: str, respuesta: str) -> bool:
        Publicaciones.db.connect()  # Conecta a la base de datos
        try:
            query = f"UPDATE {Publicaciones.tabla} SET pregunta = '{pregunta}', respuesta = '{respuesta}' WHERE id = {quest_id}"
            Publicaciones.db.execute(query)
            Publicaciones.db.connection.commit()
            return True
        except:
            return False
        finally:
            Publicaciones.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def delete(quest_id: int) -> bool:
        Publicaciones.db.connect()  # Conecta a la base de datos
        try:
            query = f"DELETE FROM {Publicaciones.tabla} WHERE id = {quest_id}"
            Publicaciones.db.execute(query)
            Publicaciones.db.connection.commit()
            return True
        except:
            return False
        finally:
            Publicaciones.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def get_all() -> List[ResponsePublicacion]:
        try:
            Publicaciones.db.connect()  # Conecta a la base de datos
            query = f"SELECT * FROM {Publicaciones.tabla}"
            result = Publicaciones.db.execute(query)


            if not result:
                return []

            rows = [ResponsePublicacion(

                cod_oferta=row[0],
                nom_oferta=row[1],
                rut_empr=row[2],
                cod_pais=row[3],
                cod_city=row[4],
                cod_cargo=row[5],
                cod_sucu=row[6],
                cod_turno=row[7],
                fecha=row[8],
                fecha_pub=row[9],
                fecha_ini=row[10],
                fecha_ter=row[11],
                sbase=row[12],
                liquido=row[13],
                bruto=row[14],
                contrato=row[15],
                carga_hora=row[16],
                nivel_lab=row[17],
                log_video=row[18],
                estado=row[19],
                fecha_hora=row[20],
                modalidad=row[21],
                ingles=row[22],
                estudios=row[23],
                licencia=row[24],
                region=row[25],
                titulo=row[26],
                experiencia=row[27],
                log_discap=row[28],
                graduado=row[29],
                descripcion=row[30],
                email_selec=row[31],
                etiqueta=row[32]

            ).dict() for row in result]

            return rows

        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
        finally:
            Publicaciones.db.close()