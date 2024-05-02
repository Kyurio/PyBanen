from app.database.Database import Conexion

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
            return result
        finally:
            db_connector.close()  # Cierra la conexión a la base de datos

    @classmethod
    def verify_user_existence(cls, email):

        db_connector = Conexion()  # Utiliza la clase de conexión
        try:
            db_connector.connect()  # Conecta a la base de datos
            query = f"SELECT * FROM {cls.tabla} WHERE email = %s"
            result = db_connector.execute(query, [email])
            print("resultados de la verificacion: ", result)
            return result
        finally:
            db_connector.close()  # Cierra la conexión a la base de datos
