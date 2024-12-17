import random
import customtkinter as ctk


def Entre(n1,n2):
    n1=n1*1000
    n2=n2*1000
    
    return random.randint(n1, n2)

def clean_widgets(self):
    for widget in self.winfo_children():
        widget.destroy()
        
class CustomDialog(ctk.CTkToplevel):
    def __init__(self, master, title="Cuadro de dialogo", message="mensaje", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.result = None  # Variable para almacenar el resultado
        self.title(title)
        self.geometry("300x150")
        self.resizable(False, False)

        # Configuración de la ventana
        self.grab_set()  # Bloquea la ventana principal mientras está abierta
        self.protocol("WM_DELETE_WINDOW", self.on_close)  # Manejar botón de cerrar

        # Vincular teclas Enter y Esc
        self.bind("<Return>", lambda event: self.on_accept())  # Enter para aceptar
        self.bind("<Escape>", lambda event: self.on_close())  # Esc para cerrar

        # Mensaje
        self.label_message = ctk.CTkLabel(self, text=message, wraplength=280, justify="center")
        self.label_message.pack(pady=(20, 10))

        # Campo de entrada
        self.entry = ctk.CTkEntry(self, width=250)
        self.entry.pack(pady=10)

        # Botones
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        self.button_accept = ctk.CTkButton(
            self.button_frame, 
            text="Aceptar", 
            command=self.on_accept,
            fg_color="green",
            text_color="white",
            hover_color="darkgreen"
        )
        self.button_accept.pack(side="left", padx=10)

        self.button_close = ctk.CTkButton(
            self.button_frame, 
            text="Cerrar", 
            command=self.on_close,
            fg_color="red",
            text_color="white",
            hover_color="darkred"
        )
        self.button_close.pack(side="left", padx=10)

    def on_accept(self):
        """Acción al presionar Aceptar."""
        if not self.entry.get().strip():  
            return
        self.result = self.entry.get()  # Guarda el contenido del Entry
        self.destroy()  # Cierra la ventana

    def on_close(self):
        """Acción al cerrar la ventana."""
        self.result = False  # Devuelve False
        self.destroy()  # Cierra la ventana

    @staticmethod
    def show(master, title, message):
        """Método estático para mostrar el cuadro de diálogo."""
        dialog = CustomDialog(master, title, message)
        dialog.wait_window()  # Espera a que la ventana se cierre
        return dialog.result
    
def space(self, n):
    self.space = ctk.CTkLabel(self, text="")
    self.space.pack(pady=n*10)