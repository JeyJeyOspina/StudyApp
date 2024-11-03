import tkinter as tk
from tkinter import ttk, messagebox
from app.model.study import Estudio, GrupoDeEstudio
from datetime import time


class VistaBuscarGrupo:
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
            text="Buscar Grupo de Estudio",
            font=("Arial", 20, "bold"),
            bg="#003366",
            fg="white"
        )
        self.titulo.pack(pady=20)

        # Frame para el formulario
        self.frame_form = tk.Frame(self.frame, bg="#003366")
        self.frame_form.pack(pady=10)

        # Campo Temática (Combobox)
        label_tematica = tk.Label(self.frame_form, text="Temática:", bg="#003366", fg="white")
        label_tematica.pack(pady=5)
        self.tematicas = ["Cálculos", "Desarrollo de Software", "Soluciones de Software",
                          "Ciencia de Datos", "Física", "Algebra"]
        self.combo_tematica = ttk.Combobox(
            self.frame_form,
            values=self.tematicas,
            width=27,
            state="readonly"
        )
        self.combo_tematica.pack(pady=5)
        self.combo_tematica.set("Seleccione una temática")

        # Campo Modalidad (Combobox)
        label_modalidad = tk.Label(self.frame_form, text="Modalidad:", bg="#003366", fg="white")
        label_modalidad.pack(pady=5)
        self.modalidades = ["Presencial", "Virtual", "Híbrido"]
        self.combo_modalidad = ttk.Combobox(
            self.frame_form,
            values=self.modalidades,
            width=27,
            state="readonly"
        )
        self.combo_modalidad.pack(pady=5)
        self.combo_modalidad.set("Seleccione una modalidad")

        # Campo Hora (Combobox)
        label_hora = tk.Label(self.frame_form, text="Hora:", bg="#003366", fg="white")
        label_hora.pack(pady=5)
        self.horas = [f"{h:02d}:00" for h in range(24)] + [f"{h:02d}:30" for h in range(24)]
        self.horas.sort()
        self.combo_hora = ttk.Combobox(
            self.frame_form,
            values=self.horas,
            width=27,
            state="readonly"
        )
        self.combo_hora.pack(pady=5)
        self.combo_hora.set("Seleccione una hora")

        # Frame para botones
        self.frame_botones = tk.Frame(self.frame, bg="#003366")
        self.frame_botones.pack(pady=20)

        # Botón Buscar
        self.btn_buscar = ttk.Button(
            self.frame_botones,
            text="Buscar Grupo",
            command=self.buscar_grupo,
            width=20
        )
        self.btn_buscar.pack(side='left', padx=5)

        # Botón Volver
        self.btn_volver = ttk.Button(
            self.frame_botones,
            text="Volver",
            command=self.volver,
            width=20
        )
        self.btn_volver.pack(side='left', padx=5)

        # Frame para resultados
        self.frame_resultados = tk.Frame(self.frame, bg="#003366")
        self.frame_resultados.pack(pady=10, expand=True, fill='both')

    def buscar_grupo(self):
        tematica = self.combo_tematica.get()
        modalidad = self.combo_modalidad.get()
        hora_str = self.combo_hora.get()

        # Validaciones
        if tematica not in self.tematicas:
            messagebox.showerror("Error", "Debe seleccionar una temática válida.")
            return

        if modalidad not in self.modalidades:
            messagebox.showerror("Error", "Debe seleccionar una modalidad válida.")
            return

        if hora_str not in self.horas:
            messagebox.showerror("Error", "Debe seleccionar una hora válida.")
            return

        hora, minuto = map(int, hora_str.split(':'))
        horario = time(hour=hora, minute=minuto)

        resultado = self.estudio.buscar_grupo_de_estudio(tematica, modalidad, horario)

        self.mostrar_resultados(resultado)

    def mostrar_resultados(self, resultado):
        # Limpiar resultados anteriores
        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        if isinstance(resultado, GrupoDeEstudio):
            tk.Label(
                self.frame_resultados,
                text=f"Grupo encontrado: {resultado.nombre}",
                bg="#003366",
                fg="white",
                font=("Arial", 12, "bold")
            ).pack(pady=5)
            tk.Label(
                self.frame_resultados,
                text=f"Temática: {resultado.tematica}",
                bg="#003366",
                fg="white"
            ).pack()
            tk.Label(
                self.frame_resultados,
                text=f"Modalidad: {resultado.modalidad}",
                bg="#003366",
                fg="white"
            ).pack()
            tk.Label(
                self.frame_resultados,
                text=f"Horario: {resultado.horario.strftime('%H:%M')}",
                bg="#003366",
                fg="white"
            ).pack()
        else:
            tk.Label(
                self.frame_resultados,
                text=resultado,
                bg="#003366",
                fg="white",
                wraplength=300
            ).pack(pady=10)

    def volver(self):
        self.frame.destroy()
        self.callback_volver()

    def destroy(self):
        self.frame.destroy()