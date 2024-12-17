# FILE: main.py
import customtkinter as ctk
from gui.main_window import MainWindow
from utils.test.notify import success, error, info

def main():
    try:
        info("Iniciando la aplicación...")
        app = MainWindow()
        app.mainloop()
        success("La aplicación se cerró correctamente.")
    except Exception as e:
        error(f"Error en la aplicación: {e}")

if __name__ == "__main__":
    main()