# FILE: DATA/DAO/database_manager.py
import os
import sqlite3
from utils.test.notify import success, error, info, warning

class DatabaseManager:
    def __init__(self, db_name):
        self.db_path = os.path.join(f"DATA/DB/{db_name}")
        self.init_database()

    def init_database(self):
        """Inicializa la base de datos y crea las tablas necesarias."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                # Tabla de personajes
                cursor.execute('''CREATE TABLE IF NOT EXISTS characters (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT UNIQUE NOT NULL
                                )''')

                # Tabla de carpetas de sprites asociadas a personajes
                cursor.execute('''CREATE TABLE IF NOT EXISTS sprite_folders (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    character_id INTEGER NOT NULL,
                                    folder_name TEXT NOT NULL,
                                    FOREIGN KEY (character_id) REFERENCES characters (id)
                                )''')

                success("Base de datos inicializada correctamente.")
        except Exception as e:
            error(f"Error al inicializar la base de datos: {e}")

    def add_sprite_folder(self, character_id, folder_name):
        """Agrega una carpeta de sprites asociada a un personaje."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO sprite_folders (character_id, folder_name) VALUES (?, ?)', 
                            (character_id, folder_name))
                conn.commit()
                success(f"Carpeta '{folder_name}' agregada para el personaje con ID {character_id}.")
                return True
        except Exception as e:
            error(f"Error al agregar carpeta de sprites: {e}")
            return False

    def get_sprite_folders(self, character_id):
        """Obtiene las carpetas de sprites de un personaje."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT folder_name FROM sprite_folders WHERE character_id = ?", (character_id,))
                rows = cursor.fetchall()
                return [row[0] for row in rows]
        except Exception as e:
            error(f"Error al obtener carpetas de sprites: {e}")
            return []


    def get_characters(self):
        """Obtiene la lista de personajes almacenados."""
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
        """Agrega un nuevo personaje a la base de datos."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO characters (name) VALUES (?)", (name,))
                conn.commit()
                success(f"Personaje '{name}' agregado a la base de datos.")
                return True
        except sqlite3.IntegrityError:
            warning(f"El personaje '{name}' ya existe.")
            return False
        except Exception as e:
            error(f"Error al agregar personaje: {e}")
            return False

    def delete_character(self, character_id):
        """Elimina un personaje de la base de datos."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM characters WHERE id = ?", (character_id,))
                if cursor.rowcount > 0:
                    conn.commit()
                    success(f"Personaje con ID {character_id} eliminado correctamente.")
                    return True
                else:
                    warning(f"No se encontró un personaje con ID {character_id}.")
                    return False
        except Exception as e:
            error(f"Error al eliminar personaje: {e}")
            return False

    def update_character(self, character_id, new_name):
        """Actualiza el nombre de un personaje en la base de datos."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE characters SET name = ? WHERE id = ?", (new_name, character_id))
                if cursor.rowcount > 0:
                    conn.commit()
                    success(f"Personaje con ID {character_id} actualizado a '{new_name}'.")
                    return True
                else:
                    warning(f"No se encontró un personaje con ID {character_id}.")
                    return False
        except sqlite3.IntegrityError:
            warning(f"Ya existe un personaje con el nombre '{new_name}'.")
            return False
        except Exception as e:
            error(f"Error al actualizar personaje: {e}")
            return False

    def search_character(self, name):
        """Busca personajes por nombre (búsqueda parcial)."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                query = f"%{name}%"
                cursor.execute("SELECT id, name FROM characters WHERE name LIKE ?", (query,))
                rows = cursor.fetchall()
                return [{"id": row[0], "name": row[1]} for row in rows]
        except Exception as e:
            error(f"Error al buscar personaje: {e}")
            return []

    def reset_database(self):
        """Elimina todas las tablas de la base de datos (reinicio completo)."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DROP TABLE IF EXISTS characters")
                cursor.execute("DROP TABLE IF EXISTS character_metadata")
                conn.commit()
                success("Base de datos reiniciada correctamente.")
                self.init_database()
        except Exception as e:
            error(f"Error al reiniciar la base de datos: {e}")

    def get_character_metadata(self, character_id):
        """Obtiene los metadatos asociados a un personaje."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT key, value FROM character_metadata WHERE character_id = ?", (character_id,))
                rows = cursor.fetchall()
                return {row[0]: row[1] for row in rows}
        except Exception as e:
            error(f"Error al obtener metadatos del personaje: {e}")
            return {}

    def add_character_metadata(self, character_id, key, value):
        """Agrega o actualiza metadatos para un personaje."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO character_metadata (character_id, key, value)
                                VALUES (?, ?, ?)
                                ON CONFLICT(character_id, key) DO UPDATE SET value = excluded.value''',
                                (character_id, key, value))
                conn.commit()
                success(f"Metadato '{key}' agregado/actualizado para el personaje con ID {character_id}.")
                return True
        except Exception as e:
            error(f"Error al agregar metadato: {e}")
            return False

    def close_connection(self):
        """Método para cerrar conexiones (si se usa fuera de contexto)."""
        try:
            self.conn.close()
            info("Conexión a la base de datos cerrada correctamente.")
        except AttributeError:
            warning("No hay conexiones abiertas que cerrar.")
