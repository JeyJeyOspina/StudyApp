import tkinter as tk
from tkinter import ttk
from app.model.study import Estudio, GrupoDeEstudio

class VistaVerGrupos:
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
            text="Grupos de Estudio",
            font=("Arial", 20, "bold"),
            bg="#003366",
            fg="white"
        )
        self.titulo.pack(pady=20)

        # Frame para filtros
        self.frame_filtros = tk.Frame(self.frame, bg="#003366")
        self.frame_filtros.pack(pady=10)

        # Filtro por Temática
        label_tematica = tk.Label(self.frame_filtros, text="Temática:", bg="#003366", fg="white")
        label_tematica.grid(row=0, column=0, padx=5, pady=5)
        self.tematicas = ["Todas", "Cálculos", "Desarrollo de Software", "Soluciones de Software",
                          "Ciencia de Datos", "Física", "Algebra"]
        self.combo_tematica = ttk.Combobox(
            self.frame_filtros,
            values=self.tematicas,
            width=20,
            state="readonly"
        )
        self.combo_tematica.grid(row=0, column=1, padx=5, pady=5)
        self.combo_tematica.set("Todas")

        # Filtro por Modalidad
        label_modalidad = tk.Label(self.frame_filtros, text="Modalidad:", bg="#003366", fg="white")
        label_modalidad.grid(row=0, column=2, padx=5, pady=5)
        self.modalidades = ["Todas", "Presencial", "Virtual", "Híbrido"]
        self.combo_modalidad = ttk.Combobox(
            self.frame_filtros,
            values=self.modalidades,
            width=20,
            state="readonly"
        )
        self.combo_modalidad.grid(row=0, column=3, padx=5, pady=5)
        self.combo_modalidad.set("Todas")

        # Botón de Filtrar
        self.btn_filtrar = ttk.Button(
            self.frame_filtros,
            text="Filtrar",
            command=self.filtrar_grupos,
            width=15
        )
        self.btn_filtrar.grid(row=0, column=4, padx=5, pady=5)

        # Frame para la lista de grupos
        self.frame_lista = tk.Frame(self.frame, bg="#003366")
        self.frame_lista.pack(pady=10, expand=True, fill='both')

        # Crear Treeview
        self.tree = ttk.Treeview(self.frame_lista, columns=('Nombre', 'Temática', 'Modalidad', 'Horario'), show='headings')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Temática', text='Temática')
        self.tree.heading('Modalidad', text='Modalidad')
        self.tree.heading('Horario', text='Horario')
        self.tree.pack(side=tk.LEFT, expand=True, fill='both')

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.frame_lista, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Botón Volver
        self.btn_volver = ttk.Button(
            self.frame,
            text="Volver",
            command=self.volver,
            width=20
        )
        self.btn_volver.pack(pady=10)

        # Cargar grupos inicialmente
        self.cargar_grupos()

    def cargar_grupos(self):
        # Limpiar el Treeview
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Cargar todos los grupos
        for grupo in self.estudio.grupos_de_estudio:
            self.tree.insert('', 'end', values=(
                grupo.nombre,
                grupo.tematica,
                grupo.modalidad,
                grupo.horario.strftime('%H:%M')
            ))

    def filtrar_grupos(self):
        tematica = self.combo_tematica.get()
        modalidad = self.combo_modalidad.get()

        # Limpiar el Treeview
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Aplicar filtros
        for grupo in self.estudio.grupos_de_estudio:
            if (tematica == "Todas" or grupo.tematica == tematica) and \
               (modalidad == "Todas" or grupo.modalidad == modalidad):
                self.tree.insert('', 'end', values=(
                    grupo.nombre,
                    grupo.tematica,
                    grupo.modalidad,
                    grupo.horario.strftime('%H:%M')
                ))

    def volver(self):
        self.frame.destroy()
        self.callback_volver()

    def destroy(self):
        self.frame.destroy()