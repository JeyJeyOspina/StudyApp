import tkinter as tk
from tkinter import ttk, messagebox
from app.model.study import Estudio

class VistaRegistro:
    def __init__(self, root, callback_volver):
        self.root = root
        self.estudio = Estudio()
        self.frame_registro = tk.Frame(self.root, bg="#003366")
        self.frame_registro.pack(expand=True, padx=20, pady=20)

        # Estilos
        self.label_style = {'bg': "#003366", 'fg': "white"}
        self.button_style = {'width': 20}

        # Campos del formulario
        campos = [("Nombre:", "entry_nombre"), ("Correo:", "entry_correo"),
                  ("ID:", "entry_id"), ("Carrera:", "entry_carrera"),
                  ("Semestre Actual:", "entry_semestre")]

        for texto, atributo in campos:
            label = tk.Label(self.frame_registro, text=texto, **self.label_style)
            label.pack(pady=5)
            entry = ttk.Entry(self.frame_registro)
            entry.pack(pady=5)
            setattr(self, atributo, entry)

        # Botón para registrar
        self.boton_registrar = ttk.Button(self.frame_registro, text="Registrar",
                                          command=self.registrar_estudiante, **self.button_style)
        self.boton_registrar.pack(pady=10)

        # Botón Volver
        self.boton_volver = ttk.Button(self.frame_registro, text="Volver",
                                       command=callback_volver, **self.button_style)
        self.boton_volver.pack(pady=5)

    def registrar_estudiante(self):
        # Obtener los datos del formulario
        nombre = self.entry_nombre.get().strip()
        correo = self.entry_correo.get().strip()
        id_str = self.entry_id.get().strip()
        carrera = self.entry_carrera.get().strip()
        semestre_str = self.entry_semestre.get().strip()

        # Validar los datos
        if not nombre or not correo or not id_str or not carrera or not semestre_str:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            id = int(id_str)
            semestre = int(semestre_str)
        except ValueError:
            messagebox.showerror("Error", "ID y Semestre deben ser números.")
            return

        # Se llama al metodo
        self.estudio.registrar_estudiante(nombre, correo, id, carrera, semestre)
        messagebox.showinfo("Registro exitoso", "Estudiante registrado correctamente")

    def destroy(self):
        self.frame_registro.destroy()