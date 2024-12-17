import os
import sqlite3
from utils.test.notify import success, error

class DatabaseManager:
    def __init__(self):
        self.db_path = os.path.join("DATA", "DB", "characters.db")
        self.init_database()

    def init_database(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS characters (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT UNIQUE NOT NULL
                                    )''')
                success("Base de datos inicializada correctamente.")
        except Exception as e:
            error(f"Error al inicializar la base de datos: {e}")

    def get_characters(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM characters")
                rows = cursor.fetchall()
                return [row[0] for row in rows]
        except Exception as e:
            error(f"Error al obtener personajes: {e}")
            return []

    def add_character(self, name):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO characters (name) VALUES (?)", (name,))
                conn.commit()
                success(f"Personaje '{name}' agregado a la base de datos.")
                return True
        except sqlite3.IntegrityError:
            error(f"El personaje '{name}' ya existe.")
            return False
        except Exception as e:
            error(f"Error al agregar personaje: {e}")
            return False
