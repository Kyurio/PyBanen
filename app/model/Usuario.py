from typing import List
from app.database.Database import Conexion
from app.schema.SchemaUsuario import UsuariosResponse


class Usuarios:

    db = Conexion()
    tabla = "reclu120"

    @staticmethod
    def create(data: dict) -> bool:

        print("request modelo ", data)
        Usuarios.db.connect()
        try:
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            query = f"INSERT INTO {Usuarios.tabla} ({columns}) VALUES ({placeholders})"
            Usuarios.db.execute(query, list(data.values()))
            Usuarios.db.connection.commit()
            return True
        except Exception as e:
            print(f"Error al insertar en la base de datos: {e}")
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
    def delete(id: int) -> bool:
        Usuarios.db.connect()
        try:
            query = f"DELETE FROM {Usuarios.tabla} WHERE id = {id}"
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

            usuarios_response = []

            for usuario_data in result:
                usuario_response = UsuariosResponse(
                    rut_post=usuario_data[0],
                    nom_post=usuario_data[1],
                    paterno=usuario_data[2],
                    materno=usuario_data[3],
                    nombre=usuario_data[4],
                    titulo=usuario_data[5],
                    clave=usuario_data[6],
                    fecha_nac=usuario_data[7],
                    tipo_doc=int(usuario_data[8]),
                    log_licen=int(usuario_data[9]),
                    log_movil=int(usuario_data[10]),
                    fono1=usuario_data[11],
                    fono2=usuario_data[12],
                    direccion=usuario_data[13],
                    id_comuna=int(usuario_data[14]),
                    id_region=int(usuario_data[15]),
                    id_provincia=int(usuario_data[16]),
                    email=usuario_data[17],
                    sbase=int(usuario_data[18]),
                    liquido=int(usuario_data[19]),
                    bruto=int(usuario_data[20]),
                    estado=int(usuario_data[21]),
                    created_at=usuario_data[22],
                    updated_at=usuario_data[23]
                )
                usuarios_response.append(usuario_response)

            return usuarios_response

        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
        finally:
            Usuarios.db.close()
