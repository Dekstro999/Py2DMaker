# FILE: gui/main_window.py
import customtkinter as ctk
from utils.metodos import clean_widgets, space
from utils.colors import *

class MainWindow(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        

    def create_widgets(self):
        clean_widgets(self)
        
        self.pack(fill="both", expand=True)
        
        self.format=("Arial", 30, "bold")
        
        space(self, 1)
        self.load_assets_button = ctk.CTkButton(self, text="Cargar Assets", command=self.parent.open_assets_window,
                                                font=self.format)
        self.load_assets_button.pack(pady=10)

        self.build_mode_button = ctk.CTkButton(self, text="Modo Construir",
                                                    fg_color=DARK_GREEN, 
                                                    text_color=WHITE,
                                                    hover_color="green",
                                                    font=self.format)
        self.build_mode_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(self, text="Salir", command=self.quit, 
                                            fg_color=DARK_RED, 
                                            text_color=WHITE,
                                            hover_color=RED,
                                            font=self.format)
        self.exit_button.pack(pady=10)
