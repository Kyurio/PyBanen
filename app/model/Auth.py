from app.database.Database import Conexion
from app.schema.SchemaUsuario import UsuariosResponse


class Auth:
    tabla = "reclu120"

    @classmethod
    def authenticate(cls, email, clave):

        print("parametros recibidos en el modelo: ", email, clave)

        db_connector = Conexion()  # Utiliza la clase de conexión
        try:
            db_connector.connect()  # Conecta a la base de datos
            query = f"SELECT * FROM {cls.tabla} WHERE email= %s AND clave = %s"
            result = db_connector.execute(query, [email, clave])

            if not result:  # Verificar si la lista está vacía
                return None  # Devolver None si la autenticación falla

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

        finally:
            db_connector.close()  # Cierra la conexión a la base de datos
