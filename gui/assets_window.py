import os
import customtkinter as ctk
from tkinter import simpledialog, messagebox
from utils.file_manager import create_folder
from utils.metodos import clean_widgets


class AssetsWindow(ctk.CTkFrame):
    def __init__(self, parent, db_manager):
        super().__init__(parent)
        self.db_manager = db_manager
        self.parent = parent
        
        # Configuración inicial del frame

    def create_widgets(self):
        clean_widgets(self)
        
        self.pack(fill="both", expand=True)
        
        # Aquí se define el contenido de la ventana de assets
        self.search_frame = ctk.CTkFrame(self, corner_radius=10)
        self.search_frame.pack(side="top", fill="x", padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Buscar personaje...")
        self.search_entry.pack(fill="x", padx=5, pady=5)
        self.search_entry.bind("<KeyRelease>", self.search_characters)

        self.listbox_frame = ctk.CTkFrame(self, corner_radius=10)
        self.listbox_frame.pack(side="left", fill="both", padx=10, pady=10)

        self.character_list_frame = ctk.CTkScrollableFrame(self.listbox_frame, width=150, height=400)
        self.character_list_frame.pack(padx=5, pady=5, fill="both", expand=True)

        self.character_buttons = []

        self.add_character_button = ctk.CTkButton(self, text="Nuevo Personaje", command=self.add_new_character)
        self.add_character_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Regresar", command=self.go_back)
        self.back_button.pack(pady=10)
    
    def create_btns(self):
        
        pass
        

    def load_characters(self):
        for button in self.character_buttons:
            button.destroy()
        self.character_buttons.clear()

        characters = self.db_manager.get_characters()
        for character in characters:
            btn = ctk.CTkButton(self.character_list_frame, text=character, command=lambda c=character: self.select_character(c))
            btn.pack(pady=2, padx=5, fill="x")
            self.character_buttons.append(btn)

    def search_characters(self, event=None):
        search_query = self.search_entry.get().lower()

        filtered_characters = [character for character in self.db_manager.get_characters() if search_query in character.lower()]

        for button in self.character_buttons:
            button.destroy()
        self.character_buttons.clear()

        for character in filtered_characters:
            btn = ctk.CTkButton(self.character_list_frame, text=character, command=lambda c=character: self.select_character(c))
            btn.pack(pady=2, padx=5, fill="x")
            self.character_buttons.append(btn)

    def add_new_character(self):
        name = simpledialog.askstring("Nuevo Personaje", "Ingrese el nombre del personaje:")
        if name:
            success = self.db_manager.add_character(name)
            if success:
                folder_path = os.path.join("assets", "characters", name)
                create_folder(folder_path)
                messagebox.showinfo("Éxito", f"Personaje '{name}' agregado correctamente.")
                self.load_characters()
            else:
                messagebox.showwarning("Error", f"El personaje '{name}' ya existe.")

    def select_character(self, name):
        messagebox.showinfo("Personaje Seleccionado", f"Seleccionaste: {name}")

    def go_back(self):
        clean_widgets(self)
        self.parent.back_to_main_window()
        pass