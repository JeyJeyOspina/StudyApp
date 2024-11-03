import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class VistaPrincipal:
    def __init__(self, root, callback_cerrar_sesion):
        self.root = root
        self.callback_cerrar_sesion = callback_cerrar_sesion

        # Frame principal
        self.frame = tk.Frame(self.root, bg="#003366")
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Estilos
        self.label_style = {'bg': "#003366", 'fg': "white"}
        self.button_style = {'width': 20}

        # Título
        self.titulo = tk.Label(
            self.frame,
            text="Panel Principal",
            font=("Arial", 20, "bold"),
            **self.label_style
        )
        self.titulo.pack(pady=20)

        # Frame para los botones de funcionalidades
        self.frame_botones = tk.Frame(self.frame, bg="#003366")
        self.frame_botones.pack(pady=20)

        # Botones de funcionalidades
        self.botones = [
            ("Ver Grupos de Estudio", self.ver_grupos),
            ("Crear Grupo de Estudio", self.crear_grupo),
            ("Ver Calendario", self.ver_calendario),
            ("Ver Planes de Estudio", self.ver_planes),
            ("Realizar Examen", self.realizar_examen),
            ("Cerrar Sesión", self.callback_cerrar_sesion)
        ]

        for texto, comando in self.botones:
            btn = ttk.Button(
                self.frame_botones,
                text=texto,
                command=comando,
                width=25
            )
            btn.pack(pady=5)

    def ver_grupos(self):
        # Implementar vista de grupos de estudio
        messagebox.showinfo("Grupos de Estudio", "Función en desarrollo")

    def crear_grupo(self):
        # Implementar creación de grupo de estudio
        messagebox.showinfo("Crear Grupo", "Función en desarrollo")

    def ver_calendario(self):
        # Implementar vista del calendario
        messagebox.showinfo("Calendario", "Función en desarrollo")

    def ver_planes(self):
        # Implementar vista de planes de estudio
        messagebox.showinfo("Planes de Estudio", "Función en desarrollo")

    def realizar_examen(self):
        # Implementar vista de exámenes
        messagebox.showinfo("Exámenes", "Función en desarrollo")

    def destroy(self):
        self.frame.destroy()