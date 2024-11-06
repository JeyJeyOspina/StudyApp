import tkinter as tk
from tkinter import ttk, messagebox
from app.model.study import Estudio, Usuario


class VistaLogin:
    def __init__(self, root, callback_volver, callback_login_exitoso):
        self.root = root
        self.estudio = Estudio()
        self.callback_login_exitoso = callback_login_exitoso
        self.usuario: Usuario = Usuario("x","x",2,"x",2)

        self.label_style = {'bg': "#003366", 'fg': "white", 'font': ('Arial', 11)}
        self.entry_style = {'width': 30}

        self.frame = tk.Frame(self.root, bg="#003366")
        self.frame.pack(expand=True, padx=20, pady=20)

        # Título
        self.titulo = tk.Label(
            self.frame,
            text="Iniciar Sesión",
            font=("Arial", 16, "bold"),
            bg="#003366",
            fg="white"
        )
        self.titulo.pack(pady=20)

        # Frame para el formulario
        self.frame_formulario = tk.Frame(self.frame, bg="#003366")
        self.frame_formulario.pack(pady=10)

        # Campo de correo
        self.frame_correo = tk.Frame(self.frame_formulario, bg="#003366")
        self.frame_correo.pack(pady=5)

        self.label_correo = tk.Label(
            self.frame_correo,
            text="Correo:",
            **self.label_style
        )
        self.label_correo.pack(side=tk.LEFT, padx=5)

        self.entry_correo = ttk.Entry(
            self.frame_correo,
            **self.entry_style
        )
        self.entry_correo.pack(side=tk.LEFT, padx=5)

        # Campo de ID
        self.frame_id = tk.Frame(self.frame_formulario, bg="#003366")
        self.frame_id.pack(pady=5)

        self.label_id = tk.Label(
            self.frame_id,
            text="ID:",
            **self.label_style
        )
        self.label_id.pack(side=tk.LEFT, padx=5)

        self.entry_id = ttk.Entry(
            self.frame_id,
            show="*",
            **self.entry_style
        )
        self.entry_id.pack(side=tk.LEFT, padx=5)

        # Frame para botones
        self.frame_botones = tk.Frame(self.frame, bg="#003366")
        self.frame_botones.pack(pady=20)

        # Botón de inicio de sesión
        self.boton_login = ttk.Button(
            self.frame_botones,
            text="Iniciar Sesión",
            command=self.iniciar_sesion,
            width=25
        )
        self.boton_login.pack(pady=10)

        # Botón volver
        self.boton_volver = ttk.Button(
            self.frame_botones,
            text="Volver",
            command=callback_volver,
            width=25
        )
        self.boton_volver.pack(pady=5)

    def iniciar_sesion(self):
        correo = self.entry_correo.get().strip()
        id_str = self.entry_id.get().strip()

        if not correo or not id_str:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return

        try:
            id = int(id_str)
            if self.estudio.iniciar_sesion(correo, id):
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
                self.usuario = self.estudio.iniciar_sesion(correo, id)
                self.callback_login_exitoso()
            else:
                messagebox.showerror("Error", "Correo o ID incorrectos")
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número")

    def destroy(self):
        self.frame.destroy()