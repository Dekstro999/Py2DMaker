# FILE: main.py
import customtkinter as ctk
from gui.main_window import MainWindow
from gui.assets_window import AssetsWindow
from utils.test.notify import success, error, info

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Ventana Principal")
        self.geometry("800x600")
        
        self.main_window = MainWindow(self)
        # self.main_window.pack(fill="both", expand=True)
        
        self.main_window.create_widgets()
        
        self.assets_window = AssetsWindow(self)

    def open_assets_window(self):
        # self.assets_window.pack(fill="both", expand=True)
        self.main_window.pack_forget()

        self.assets_window.create_widgets()
        self.assets_window.load_characters()

    def back_to_main_window(self):
        self.assets_window.pack_forget()  
        # self.main_window.pack(fill="both", expand=True) 
        self.main_window.create_widgets()
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
