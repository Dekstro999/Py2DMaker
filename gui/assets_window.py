import customtkinter as ctk
from DATA.DAO.database_manager import DatabaseManager
from tkinter import simpledialog, messagebox
from utils.file_manager import create_folder
import os


class AssetsWindow(ctk.CTkFrame):
    def __init__(self, parent, db_base):
        super().__init__(parent)
        self.db_manager = db_base

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        self.left_frame = ctk.CTkFrame(self, width=200)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.character_list = ctk.CTkScrollableFrame(self.left_frame)
        self.character_list.pack(fill="both", expand=True)

        self.new_character_button = ctk.CTkButton(
            self.left_frame, text="Nuevo Personaje", command=self.add_new_character
        )
        self.new_character_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(self, text="Salir", command=self.quit)
        self.exit_button.pack(pady=10)

        self.load_characters()

    def load_characters(self):
        for widget in self.character_list.winfo_children():
            widget.destroy()

        characters = self.db_manager.get_characters()
        for character in characters:
            label = ctk.CTkLabel(self.character_list, text=character)
            label.pack(pady=2)
            label.bind("<Button-1>", self.on_character_click)

    def on_character_click(self, event):
        character_name = event.widget.cget("text")
        messagebox.showinfo("Personaje seleccionado", f"Has seleccionado: {character_name}")


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


    def on_close(self):
        self.db_manager.close()
        self.quit()
