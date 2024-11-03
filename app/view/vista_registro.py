
from tkinter import ttk, messagebox
from app.model.study import Estudio

class VistaRegistro:
    def __init__(self, root, callback_volver):
        self.root = root
        self.estudio = Estudio()  # Instancia de Estudio

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

        # Botón Volver
        self.boton_volver = ttk.Button(self.frame_registro, text="Volver", command=callback_volver)
        self.boton_volver.pack(pady=5)

    def registrar_estudiante(self):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        id = int(self.entry_id.get())
        carrera = self.entry_carrera.get()
        semestre_actual = int(self.entry_semestre.get())

        exito = self.estudio.registrar_estudiante(nombre, id, correo, carrera, semestre_actual)
        if exito:
            messagebox.showinfo("Éxito", "Estudiante registrado con éxito.")
            self.frame_registro.destroy()  # Cerrar el formulario después de registrar
        else:
            messagebox.showerror("Error", "No se pudo registrar al estudiante.")

    def destroy(self):
        self.frame_registro.destroy() #Metodo para destruir la vista del registro