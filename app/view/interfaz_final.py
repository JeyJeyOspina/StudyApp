import tkinter as tk
from app.view.vista_inicial import VistaInicial
from app.view.vista_registro import VistaRegistro

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calendario de Eventos")
        self.root.geometry("400x300")

    def run(self):
        # Inicializar la vista inicial
        self.vista_inicial = VistaInicial(self.root, self.cambiar_a_vista_registro)
        self.root.mainloop()

    def cambiar_a_vista_registro(self):
        self.vista_inicial.destroy()  # Destruir la vista inicial
        self.vista_registro = VistaRegistro(self.root, self.volver_a_vista_inicial)  # Pasar callback

    def volver_a_vista_inicial(self):
        self.vista_registro.destroy()  # Destruir la vista de registro
        self.vista_inicial = VistaInicial(self.root, self.cambiar_a_vista_registro)  # Reiniciar la vista inicial




"""class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendario de Eventos")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        # Instancia de Estudio
        self.estudio = Estudio()

        # Marco para los botones
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack(expand=True)

        # Título
        self.titulo = ttk.Label(self.frame, text="Bienvenido al Calendario de Eventos", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Botón Iniciar sesión
        self.boton_iniciar_sesion = ttk.Button(self.frame, text="Iniciar sesión", command=self.iniciar_sesion)
        self.boton_iniciar_sesion.pack(pady=10, fill='x')

        # Botón Registrarse
        self.boton_registrarse = ttk.Button(self.frame, text="Registrarse", command=self.mostrar_formulario_registro)
        self.boton_registrarse.pack(pady=10, fill='x')

    def iniciar_sesion(self):
        print("Iniciar sesión clicado")

    def mostrar_formulario_registro(self):
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

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()"""