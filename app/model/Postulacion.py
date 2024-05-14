from app.database.Database import Conexion
from app.schema.SchemaPostulacion import ResponsePostulacion, ResponseGetPostulacion
from typing import List


class Postulacion:
    db = Conexion()  # Instancia la clase MySQLConnection
    tabla = "postulaciones"

    @staticmethod
    def create(cod_oferta: str, rut_post: str) -> int:
        Postulacion.db.connect()  # Conecta a la base de datos
        try:
            query = f"INSERT INTO {Postulacion.tabla} (cod_oferta, rut_post) VALUES ('{cod_oferta}', '{rut_post}')"
            Postulacion.db.execute(query)
            reuslt = Postulacion.db.connection.commit()
            return reuslt
        finally:
            Postulacion.db.close()  # Cierra la conexión a la base de datos

    @staticmethod
    def get(id: int) -> ResponsePostulacion:
        with Conexion() as db:
            try:
                query = f"SELECT * FROM {Postulacion.tabla} WHERE id = %s"
                result = db.execute(query, (id,))
                if result:
                    row = result[0]
                    return ResponsePostulacion(
                        id=row[0],
                        nombre_Postulacion=row[1],
                        descripcion=row[2],
                        estado=row[3],
                        created_at=row[4],
                        updated_at=row[5]
                    )
                else:
                    return False

            except Exception as e:
                print(f"Error al obtener Postulacion: {e}")
                raise

    @staticmethod
    def update(id: int, data: dict) -> bool:
        try:
            with Conexion() as db:
                columns = ', '.join([f"{key} = %s" for key in data.keys()])
                values = list(data.values())
                values.append(id)
                query = f"UPDATE {Postulacion.tabla} SET {columns}, updated_at = NOW() WHERE id = %s"
                db.execute(query, values)
                return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    @staticmethod
    def delete(quest_id: int) -> bool:
        with Conexion() as db:
            try:
                query = f"DELETE FROM {Postulacion.tabla} WHERE id = %s"
                db.execute(query, (quest_id,))
                db.connection.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar Postulacion: {e}")
                raise

    @staticmethod

    def get_all() -> List[ResponsePostulacion]:
        try:
            Postulacion.db.connect()  # Conecta a la base de datos
            query = f"SELECT * FROM {Postulacion.tabla}"
            result = Postulacion.db.execute(query)

            if not result:
                return []

            rows = []
            for row in result:
                rows.append(ResponsePostulacion(
                    id_postulacion=row[0],
                    cod_oferta=row[1],
                    rut_post=row[2],
                    created_at=row[3],
                    updated_at=row[4],
                ))
            return rows

        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
        finally:
            Postulacion.db.close()