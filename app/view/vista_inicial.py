import tkinter as tk
from tkinter import ttk

class VistaInicial:
    def __init__(self, root, callback_registro):
        self.root = root
        self.frame = tk.Frame(self.root, bg="#003366")
        self.frame.pack(expand=True, padx=20, pady=20)

        # Título
        self.titulo = tk.Label(self.frame, text="Bienvenido a Study App", font=("Arial", 16), bg="#003366", fg="white")
        self.titulo.pack(pady=10)

        # Botón Iniciar sesión
        self.boton_iniciar_sesion = tk.Button(self.frame, text="Iniciar sesión", command=self.iniciar_sesion)
        self.boton_iniciar_sesion.pack(pady=10, fill='x')

        # Botón Registrarse
        self.boton_registrarse = tk.Button(self.frame, text="Registrarse", command=callback_registro)
        self.boton_registrarse.pack(pady=10, fill='x')

    def iniciar_sesion(self):
        print("Iniciar sesión clicado")

    def destroy(self):
        self.frame.destroy()  # Destruir el marco de la vista inicial.
"""class VistaInicial:
    def __init__(self, root, callback_registro, callback_login):
        self.root = root
        self.frame = tk.Frame(self.root, bg="#003366")
        self.root.configure(bg="#f0f0f0")
        self.frame.pack(expand=True, padx=20, pady=20)

        # Agregar estilos consistentes
        self.button_style = {'font': ('Arial', 12), 'width': 20, 'pady': 5}

        # Mejorar el diseño del título
        self.titulo = tk.Label(
            self.frame,
            text="Bienvenido a Study App",
            font=("Arial", 20, "bold"),
            bg="#003366",
            fg="white"
        )
        self.titulo.pack(pady=20)

        # Mejorar los botones
        self.boton_iniciar_sesion = tk.Button(
            self.frame,
            text="Iniciar sesión",
            command=callback_login,
            **self.button_style
        )
        self.boton_iniciar_sesion.pack(pady=10)

        self.boton_registrarse = tk.Button(
            self.frame,
            text="Registrarse",
            command=callback_registro,
            **self.button_style
        )
        self.boton_registrarse.pack(pady=10)

    def destroy(self):
        self.frame.destroy()"""