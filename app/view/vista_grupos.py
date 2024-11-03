import tkinter as tk
from tkinter import ttk, messagebox
from app.model.study import Estudio
from datetime import time

class VistaCrearGrupo:
    def __init__(self, root, callback_volver):
        self.root = root
        self.estudio = Estudio()
        self.callback_volver = callback_volver

        # Frame principal
        self.frame = tk.Frame(self.root, bg="#003366")
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Título
        self.titulo = tk.Label(
            self.frame,
            text="Crear Grupo de Estudio",
            font=("Arial", 20, "bold"),
            bg="#003366",
            fg="white"
        )
        self.titulo.pack(pady=20)

        # Frame para el formulario
        self.frame_form = tk.Frame(self.frame, bg="#003366")
        self.frame_form.pack(pady=10)

        # Campos de texto
        campos = [
            ("Nombre:", "entry_nombre"),
            ("Temática:", "entry_tematica"),
            ("Hora (HH:MM):", "entry_hora")
        ]

        for texto, atributo in campos:
            label = tk.Label(self.frame_form, text=texto, bg="#003366", fg="white")
            label.pack(pady=5)
            entry = ttk.Entry(self.frame_form, width=30)
            entry.pack(pady=5)
            setattr(self, atributo, entry)

        # Campo Modalidad (Combobox)
        label_modalidad = tk.Label(
            self.frame_form,
            text="Modalidad:",
            bg="#003366",
            fg="white"
        )
        label_modalidad.pack(pady=5)

        self.modalidades = ["Presencial", "Virtual", "Híbrido"]
        self.combo_modalidad = ttk.Combobox(
            self.frame_form,
            values=self.modalidades,
            width=27,
            state="readonly"
        )
        self.combo_modalidad.pack(pady=5)
        self.combo_modalidad.set("Seleccione una modalidad")  # Valor por defecto

        # Frame para botones
        self.frame_botones = tk.Frame(self.frame, bg="#003366")
        self.frame_botones.pack(pady=20)

        # Botón Crear
        self.btn_crear = ttk.Button(
            self.frame_botones,
            text="Crear Grupo",
            command=self.crear_grupo,
            width=20
        )
        self.btn_crear.pack(side='left', padx=5)

        # Botón Volver
        self.btn_volver = ttk.Button(
            self.frame_botones,
            text="Volver",
            command=self.volver,
            width=20
        )
        self.btn_volver.pack(side='left', padx=5)

    def crear_grupo(self):
        nombre = self.entry_nombre.get().strip()
        tematica = self.entry_tematica.get().strip()
        modalidad = self.combo_modalidad.get()
        hora_str = self.entry_hora.get().strip()

        # Validaciones
        if not all([nombre, tematica, hora_str]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if modalidad not in self.modalidades:
            messagebox.showerror("Error", "Debe seleccionar una modalidad válida.")
            return

        try:
            hora, minuto = map(int, hora_str.split(':'))
            if not (0 <= hora <= 23 and 0 <= minuto <= 59):
                raise ValueError
            horario = time(hour=hora, minute=minuto)
        except ValueError:
            messagebox.showerror("Error", "Formato de hora incorrecto. Use HH:MM (00:00 - 23:59)")
            return

        if self.estudio.registrar_grupo_de_estudio(nombre, tematica, modalidad, horario):
            messagebox.showinfo("Éxito", "Grupo de estudio creado exitosamente.")
            self.volver()
        else:
            messagebox.showerror("Error", "No se pudo crear el grupo de estudio.")

    def volver(self):
        self.frame.destroy()
        self.callback_volver()

    def destroy(self):
        self.frame.destroy()