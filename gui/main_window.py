import customtkinter as ctk
from gui.assets_window import AssetsWindow
from DATA.DAO.database_manager import DatabaseManager

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Py2DMaker")
        self.geometry("800x600")

        self.db_manager = DatabaseManager()

        self.create_widgets()

    def create_widgets(self):
        self.load_assets_button = ctk.CTkButton(self, text="Cargar Assets", command=self.open_assets_window)
        self.load_assets_button.pack(pady=10)

        self.build_mode_button = ctk.CTkButton(self, text="Modo Construir")
        self.build_mode_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(self, text="Salir", command=self.quit)
        self.exit_button.pack(pady=10)

    def open_assets_window(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.assets_window = AssetsWindow(self, self.db_manager)
        self.assets_window.pack(fill="both", expand=True)