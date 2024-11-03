import tkinter as tk
from tkinter import ttk, messagebox
from app.model.study import Estudio, GrupoDeEstudio
from datetime import datetime


class VistaGrupos:
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

        # Frame para el Treeview
        self.frame_tree = tk.Frame(self.frame, bg="#003366")
        self.frame_tree.pack(expand=True, fill='both', padx=10, pady=10)

        # Crear Treeview
        self.tree = ttk.Treeview(
            self.frame_tree,
            columns=('Nombre', 'Temática', 'Modalidad', 'Horario'),
            show='headings'
        )

        # Configurar columnas
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Temática', text='Temática')
        self.tree.heading('Modalidad', text='Modalidad')
        self.tree.heading('Horario', text='Horario')

        # Configurar ancho de columnas
        for col in ('Nombre', 'Temática', 'Modalidad', 'Horario'):
            self.tree.column(col, width=100)

        self.tree.pack(expand=True, fill='both')

        # Frame para botones
        self.frame_botones = tk.Frame(self.frame, bg="#003366")
        self.frame_botones.pack(pady=10)

        # Botones
        self.btn_unirse = ttk.Button(
            self.frame_botones,
            text="Unirse al Grupo",
            command=self.unirse_grupo,
            width=20
        )
        self.btn_unirse.pack(side='left', padx=5)

        self.btn_detalles = ttk.Button(
            self.frame_botones,
            text="Ver Detalles",
            command=self.ver_detalles,
            width=20
        )
        self.btn_detalles.pack(side='left', padx=5)

        self.btn_volver = ttk.Button(
            self.frame_botones,
            text="Volver",
            command=self.volver,
            width=20
        )
        self.btn_volver.pack(side='left', padx=5)

        # Cargar grupos
        self.cargar_grupos()

    def cargar_grupos(self):
        # Limpiar Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Cargar grupos desde el modelo
        for grupo in self.estudio.grupos_de_estudio:
            self.tree.insert('', 'end', values=(
                grupo.nombre,
                grupo.tematica,
                grupo.modalidad,
                grupo.horario.strftime("%H:%M")
            ))

    def unirse_grupo(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Por favor, seleccione un grupo")
            return

        item = self.tree.item(seleccion[0])
        nombre_grupo = item['values'][0]

        # Aquí deberías obtener el usuario actual que está logueado
        # Por ahora mostraremos solo un mensaje
        messagebox.showinfo("Unirse a Grupo", f"Te has unido al grupo: {nombre_grupo}")

    def ver_detalles(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Por favor, seleccione un grupo")
            return

        item = self.tree.item(seleccion[0])
        valores = item['values']

        detalles = f"""
        Nombre: {valores[0]}
        Temática: {valores[1]}
        Modalidad: {valores[2]}
        Horario: {valores[3]}
        """

        messagebox.showinfo("Detalles del Grupo", detalles)

    def volver(self):
        self.frame.destroy()
        self.callback_volver()

    def destroy(self):
        self.frame.destroy()