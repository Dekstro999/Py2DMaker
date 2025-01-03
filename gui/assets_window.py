# FILE: gui/assets_window.py
import os
import customtkinter as ctk
from tkinter import messagebox
from DATA.DAO.database_manager import DatabaseManager
from utils.file_manager import create_folder, delete_folder
from utils.metodos import clean_widgets, CustomDialog
from utils.colors import *


class AssetsWindow(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.db_characters = DatabaseManager("characters.db")
        # self.db_characters = db_characters
        self.parent = parent
        self.sprite_frame = None

        
        
        # Configuración inicial del frame

    def create_widgets(self):
        self.db_characters.init_database()
        clean_widgets(self)
        
        self.scroll_main = ctk.CTkScrollableFrame(self, width=800, height=600)
        self.scroll_main.pack(fill="both", expand=True)
        
        self.pack(fill="both", expand=True)
        
        self.search_frame = ctk.CTkFrame(self.scroll_main, corner_radius=10)
        self.search_frame.pack(side="top", fill="x", padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Buscar personaje...")
        self.search_entry.pack(fill="x", padx=5, pady=5)
        self.search_entry.bind("<KeyRelease>", self.search_characters)

        self.listbox_frame = ctk.CTkFrame(self.scroll_main, corner_radius=10)
        self.listbox_frame.pack(side="left", fill="both", padx=10, pady=10)

        self.character_list_frame = ctk.CTkScrollableFrame(self.listbox_frame, width=180, height=600)
        self.character_list_frame.pack(padx=5, pady=5, fill="both", expand=True)

        self.character_buttons = []
        self.sprites_buttons = []

        button_frame = ctk.CTkFrame(self.scroll_main)
        button_frame.pack(pady=5,padx=5, fill="x")

        self.add_character_button = ctk.CTkButton(button_frame, text="Nuevo Personaje", command=self.add_new_character)
        self.add_character_button.pack(side="left", padx=0)

        self.back_button = ctk.CTkButton(button_frame, text="Regresar", command=self.go_back)
        self.back_button.pack(side="left",padx=3)
    

    def create_btns(self, frame, list, buttons=None, comando=None):
        for button in buttons:
            button.destroy()
        buttons.clear()

        for l in list:
            btn_frame = ctk.CTkFrame(frame)
            btn_frame.pack(pady=2, padx=5, fill="x")

            btn = ctk.CTkButton(btn_frame, text=f"{l}", command=lambda c=l: comando(c))
            btn.pack(side="left", fill="x", expand=True)

            delete_btn = ctk.CTkButton(btn_frame, text="X", command=lambda c=l: self.delete_character(c), fg_color="red",hover_color=DARK_RED, width=2)
            delete_btn.pack(side="right", padx=5)

            buttons.append(btn)
            buttons.append(delete_btn)
        

    def delete_character(self, name):
        character = self.db_characters.search_character(name)
        if not character:
            messagebox.showerror("Error", "No se encontró el personaje en la base de datos.")
        else:
            sprite_folders = self.db_characters.get_sprite_folders(character[0]["id"])
            if not sprite_folders:
                messagebox.showwarning("Advertencia", f"El personaje '{name}' no tiene carpetas de sprites asociadas.")
                return

        character_id = character[0]["id"]

        # Eliminar carpetas de sprites asociadas
        sprite_folders = self.db_characters.get_sprite_folders(character_id)
        for folder in sprite_folders:
            folder_path = os.path.join("assets", "characters", name, folder)
            delete_folder(folder_path)

        # Eliminar la carpeta del personaje
        character_folder_path = os.path.join("assets", "characters", name)
        delete_folder(character_folder_path)

        # Eliminar el personaje de la base de datos
        success = self.db_characters.delete_character(character_id)
        if success:
            messagebox.showinfo("Éxito", f"Personaje '{name}' eliminado correctamente.")
            self.create_widgets()
            self.load_characters()
        else:
            messagebox.showwarning("Error", f"No se pudo eliminar el personaje '{name}'.")
            success = self.db_characters.delete_sprite_folder(character_id, folder)
            if success:
                messagebox.showinfo("Éxito", f"Carpeta '{folder}' eliminada correctamente.")
                self.select_character(name)
            else:
                messagebox.showwarning("Error", f"No se pudo eliminar la carpeta '{folder}'.")
            
    def load_characters(self):
        characters = self.db_characters.get_characters()
        
        self.create_btns(self.character_list_frame, characters, self.character_buttons, self.select_character)

    def search_characters(self, event=None):
        search_query = self.search_entry.get().lower()

        filtered_characters = [character for character in self.db_characters.get_characters() if search_query in character.lower()]

        self.create_btns(self.character_list_frame, filtered_characters, self.character_buttons, self.select_character)

    def add_new_character(self):
        name = CustomDialog.show(self, "Nuevo Personaje", "Ingresa el nombre del nuevo personaje")
        if name:
            success = self.db_characters.add_character(name)
            if success:
                folder_path = os.path.join("assets", "characters", name)
                create_folder(folder_path)
                messagebox.showinfo("Éxito", f"Personaje '{name}' agregado correctamente.")
                self.load_characters()
            else:
                messagebox.showwarning("Error", f"El personaje '{name}' ya existe.")
        
    def add_sprite_folder(self, character_id, character_name):
        """Agrega una nueva carpeta de sprites para el personaje seleccionado."""
        folder_name = CustomDialog.show(self, "Nueva Carpeta", "Ingresa el nombre de la carpeta de sprites:")
        if folder_name:
            # Agregar la carpeta a la base de datos
            success = self.db_characters.add_sprite_folder(character_id, folder_name)
            if success:
                # Crear la carpeta físicamente en el sistema de archivos
                folder_path = os.path.join("assets", "characters", character_name, folder_name)
                create_folder(folder_path)
                messagebox.showinfo("Éxito", f"Carpeta '{folder_name}' creada correctamente.")
                self.select_character(character_name)  # Recargar la vista del personaje
            else:
                messagebox.showwarning("Error", f"No se pudo crear la carpeta '{folder_name}'.")


    def select_character(self, name):
        """Muestra las carpetas de sprites asociadas al personaje seleccionado."""
        if self.sprite_frame:
            # clean_widgets(self.sprite_frame)
            self.sprite_frame.destroy()
        # self.pack(fill="both", expand=True)

        character = self.db_characters.search_character(name)
        if not character:
            messagebox.showerror("Error", "No se encontró el personaje en la base de datos.")
            return

        character_id = character[0]["id"]

        self.sprite_frame = ctk.CTkFrame(self.scroll_main, corner_radius=10)
        self.sprite_frame.pack(side="left", fill="both", padx=10, pady=10)

        self.title_label = ctk.CTkLabel(self.sprite_frame, text=f"{name}", font=("Arial", 20))
        self.title_label.pack(pady=10)

        add_folder_button = ctk.CTkButton(self.sprite_frame, text="Nuevo Sprite", 
                                        command=lambda: self.add_sprite_folder(character_id, name),
                                        width=20)
        add_folder_button.pack(pady=5)

        # Mostrar las carpetas de sprites asociadas
        sprite_folders_frame = ctk.CTkScrollableFrame(self.sprite_frame, width=180, height=400)
        sprite_folders_frame.pack(padx=5, pady=5, fill="both", expand=True)

        sprite_folders = self.db_characters.get_sprite_folders(character_id)
        self.create_btns(sprite_folders_frame, sprite_folders, self.sprites_buttons)
    def load_sprites(self):
        pass

    def go_back(self):
        clean_widgets(self)
        self.db_characters.close_connection()
        self.parent.back_to_main_window()
        pass