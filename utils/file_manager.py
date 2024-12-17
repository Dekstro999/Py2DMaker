import os
import shutil
from utils.test.notify import *

def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        success(f"Archivo copiado de {src} a {dst}")
        return True
    except Exception as e:
        error(f"Error al copiar el archivo: {e}")
        return False

def delete_file(path):
    try:
        os.remove(path)
        success(f"Archivo eliminado: {path}")
        return True
    except Exception as e:
        error(f"Error al eliminar el archivo: {e}")
        return False

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        success(f"Carpeta creada: {path}")
        return True
    except Exception as e:
        error(f"Error al crear la carpeta: {e}")
        return False

def delete_folder(path):
    try:
        shutil.rmtree(path)
        success(f"Carpeta eliminada: {path}")
        return True
    except Exception as e:
        error(f"Error al eliminar la carpeta: {e}")
        return False
