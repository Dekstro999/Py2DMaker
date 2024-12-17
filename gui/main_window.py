# FILE: gui/main_window.py
import customtkinter as ctk
from utils.metodos import clean_widgets
from utils.colors import *

class MainWindow(ctk.CTkFrame):
    def __init__(self, parent, db_manager):
        super().__init__(parent)
        self.db_manager = db_manager
        self.parent = parent
        

    def create_widgets(self):
        clean_widgets(self)
        
        self.pack(fill="both", expand=True)

        # Botón para abrir la ventana de assets
        self.load_assets_button = ctk.CTkButton(self, text="Cargar Assets", command=self.parent.open_assets_window)
        self.load_assets_button.pack(pady=10)

        # Otros botones
        self.build_mode_button = ctk.CTkButton(self, text="Modo Construir",
                                                    fg_color=DARK_GREEN, 
                                                    text_color=WHITE)
        self.build_mode_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(self, text="Salir", command=self.quit, 
                                            fg_color=DARK_RED, 
                                            text_color=WHITE)
        self.exit_button.pack(pady=10)
