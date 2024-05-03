from typing import List
from app.database.Database import Conexion
from app.schema.SchemaUsuario import UsuariosResponse


class Usuarios:

    db = Conexion()
    tabla = "reclu120"

    @staticmethod
    def create(data: dict) -> bool:

        Usuarios.db.connect()
        try:
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            query = f"INSERT INTO {Usuarios.tabla} ({columns}) VALUES ({placeholders})"
            request = Usuarios.db.execute(query, list(data.values()))
            Usuarios.db.connection.commit()

            print(request)

            if request == 0:
                return True
            else:
                return False
        except Exception as e:
            return False
        finally:
            Usuarios.db.close()

    @staticmethod
    def get(quest_id: int) -> dict:
        Usuarios.db.connect()
        try:
            query = f"SELECT * FROM {Usuarios.tabla} WHERE id = {quest_id}"
            result = Usuarios.db.execute(query)
            if result:
                return {"id_Usuarios": result[0][0], "nom_Usuarios": result[0][1], "abreviatura": result[0][2]}
            else:
                return None
        finally:
            Usuarios.db.close()

    @staticmethod
    def update(quest_id: int, pregunta: str, respuesta: str) -> bool:
        Usuarios.db.connect()
        try:
            query = f"UPDATE {Usuarios.tabla} SET pregunta = '{pregunta}', respuesta = '{respuesta}' WHERE id = {quest_id}"
            Usuarios.db.execute(query)
            Usuarios.db.connection.commit()
            return True
        except:
            return False
        finally:
            Usuarios.db.close()

    @staticmethod
    def delete(rut: str) -> bool:
        Usuarios.db.connect()
        try:
            query = f"DELETE FROM {Usuarios.tabla} WHERE rut_post = '{rut}'"
            Usuarios.db.execute(query)
            Usuarios.db.connection.commit()
            return True
        except:
            return False
        finally:
            Usuarios.db.close()

    @staticmethod
    def get_all() -> List[UsuariosResponse]:
        try:
            Usuarios.db.connect()
            query = f"SELECT * FROM {Usuarios.tabla}"
            result = Usuarios.db.execute(query)

            usuarios = []
            for result in result:
                usuario = UsuariosResponse(
                    rut_post=result[0],
                    nom_post=result[1],
                    paterno=result[2],
                    materno=result[3],
                    nombre=result[4],
                    titulo=result[5],
                    clave=result[6],
                    fecha_nac=result[7],
                    tipo_doc=result[8],
                    log_licen=result[9],
                    log_movil=result[10],
                    fono1=result[11],
                    fono2=result[12],
                    direccion=result[13],
                    id_comuna=result[14],
                    id_region=result[15],
                    id_provincia=result[16],
                    email=result[18],
                    sbase=result[17],
                    liquido=result[19],
                    bruto=result[20],
                    estado=result[21],
                    created_at=result[22],
                    updated_at=result[23]
                )
                usuarios.append(usuario)

            return usuarios

        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
        finally:
            Usuarios.db.close()
