import tkinter as tk
from tkinter import ttk, messagebox
from app.model.study import Estudio

class VistaRegistro:
    def __init__(self, root):
        self.root = root
        self.estudio = Estudio()

        self.frame_registro = ttk.Frame(self.root, padding="20")
        self.frame_registro.pack(expand=True)

        # Campos del formulario
        self.label_nombre = ttk.Label(self.frame_registro, text="Nombre:")
        self.label_nombre.pack(pady=5)
        self.entry_nombre = ttk.Entry(self.frame_registro)
        self.entry_nombre.pack(pady=5)

        self.label_correo = ttk.Label(self.frame_registro, text="Correo:")
        self.label_correo.pack(pady=5)
        self.entry_correo = ttk.Entry(self.frame_registro)
        self.entry_correo.pack(pady=5)

        self.label_id = ttk.Label(self.frame_registro, text="ID:")
        self.label_id.pack(pady=5)
        self.entry_id = ttk.Entry(self.frame_registro)
        self.entry_id.pack(pady=5)

        self.label_carrera = ttk.Label(self.frame_registro, text="Carrera:")
        self.label_carrera.pack(pady=5)
        self.entry_carrera = ttk.Entry(self.frame_registro)
        self.entry_carrera.pack(pady=5)

        self.label_semestre = ttk.Label(self.frame_registro, text="Semestre Actual:")
        self.label_semestre.pack(pady=5)
        self.entry_semestre = ttk.Entry(self.frame_registro)
        self.entry_semestre.pack(pady=5)

        # Botón para registrar
        self.boton_registrar = ttk.Button(self.frame_registro, text="Registrar", command=self.registrar_estudiante)
        self.boton_registrar.pack(pady=10)

    def registrar_estudiante(self):
        nombre = self.entry_nombre.get()
        correo = self