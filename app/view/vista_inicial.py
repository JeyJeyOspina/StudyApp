
from tkinter import ttk

class VistaInicial:
    def __init__(self, root, callback_registro):
        self.root = root
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack(expand=True)

        # Título
        self.titulo = ttk.Label(self.frame, text="Bienvenido al Calendario de Eventos", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Botón Iniciar sesión
        self.boton_iniciar_sesion = ttk.Button(self.frame, text="Iniciar sesión", command=self.iniciar_sesion)
        self.boton_iniciar_sesion.pack(pady=10, fill='x')

        # Botón Registrarse
        self.boton_registrarse = ttk.Button(self.frame, text="Registrarse", command=callback_registro)
        self.boton_registrarse.pack(pady=10, fill='x')

    def iniciar_sesion(self):
        print("Iniciar sesión clicado")

    def destroy(self):
        self.frame.destroy()  # Destruir el marco de la vista inicial