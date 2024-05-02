import os
from dotenv import load_dotenv
import mysql.connector

class Conexion:

    def __init__(self):

        current_dir = os.path.dirname(os.path.abspath(__file__))
        env_path = os.path.join(current_dir, '..', 'config', '.env')
        load_dotenv(dotenv_path=env_path)

        self.host = os.getenv("DB_HOST")
        self.username = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.connection = None
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Connected to MySQL database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    def close(self):
        if self.connection:
            self.connection.close()
            print("MySQL connection closed")
        else:
            print("No active MySQL connection")

    def execute(self, query, values=None):

        if self.connection:
            try:
                cursor = self.connection.cursor()
                if values is not None:
                    cursor.execute(query, values)
                else:
                    cursor.execute(query)
                if query.strip().lower().startswith("select"):
                    result = cursor.fetchall()
                elif query.strip().lower().startswith("insert"):
                    self.connection.commit()
                    result = cursor.lastrowid
                else:
                    self.connection.commit()
                    result = None
                cursor.close()
                return result
            except mysql.connector.Error as err:
                print(f"Error executing query: {err}")
                return None
        else:
            print("No active MySQL connection")


