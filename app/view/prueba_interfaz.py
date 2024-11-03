import tkinter as tk
from tkinter import messagebox
from app.model.study import Estudio, Usuario, Evento, Calendario  # Importar las clases necesarias


class StudyAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Study App - Entorno Académico")
        self.root.geometry("600x400")
        self.estudio = Estudio()  # Instancia de la clase principal

        # Configuración del estilo de la interfaz
        self.root.configure(bg='#f0f0f0')

        # Título
        self.title_label = tk.Label(root, text="Bienvenido a Study App", font=("Arial", 16, "bold"), bg='#f0f0f0')
        self.title_label.pack(pady=20)

        # Marco de opciones
        self.main_frame = tk.Frame(root, bg='#e0e0e0', padx=10, pady=10)
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Botones de funcionalidad
        self.create_profile_button = tk.Button(self.main_frame, text="Crear Perfil", command=self.create_profile,
                                               width=25)
        self.create_profile_button.pack(pady=5)

        self.login_button = tk.Button(self.main_frame, text="Iniciar Sesión", command=self.login, width=25)
        self.login_button.pack(pady=5)

        self.view_events_button = tk.Button(self.main_frame, text="Ver Próximos Eventos", command=self.view_events,
                                            width=25)
        self.view_events_button.pack(pady=5)

        self.quit_button = tk.Button(self.main_frame, text="Salir", command=root.quit, width=25)
        self.quit_button.pack(pady=5)

    def create_profile(self):
        # Crear una ventana emergente para el perfil
        profile_win = tk.Toplevel(self.root)
        profile_win.title("Crear Perfil")

        tk.Label(profile_win, text="Nombre").grid(row=0, column=0)
        tk.Label(profile_win, text="Correo").grid(row=1, column=0)
        tk.Label(profile_win, text="ID (Documento)").grid(row=2, column=0)
        tk.Label(profile_win, text="Carrera").grid(row=3, column=0)
        tk.Label(profile_win, text="Semestre").grid(row=4, column=0)

        # Entradas para datos del usuario
        name_entry = tk.Entry(profile_win)
        email_entry = tk.Entry(profile_win)
        id_entry = tk.Entry(profile_win)
        career_entry = tk.Entry(profile_win)
        semester_entry = tk.Entry(profile_win)

        name_entry.grid(row=0, column=1)
        email_entry.grid(row=1, column=1)
        id_entry.grid(row=2, column=1)
        career_entry.grid(row=3, column=1)
        semester_entry.grid(row=4, column=1)

        def save_profile():
            # Guardar el perfil con los datos ingresados
            nombre = name_entry.get()
            correo = email_entry.get()
            id_ = int(id_entry.get())
            carrera = career_entry.get()
            semestre = int(semester_entry.get())
            if self.estudio.registrar_estudiante(nombre, id_, correo, carrera, semestre):
                messagebox.showinfo("Éxito", "Perfil creado exitosamente")
            else:
                messagebox.showerror("Error", "No se pudo crear el perfil")
            profile_win.destroy()

        tk.Button(profile_win, text="Guardar Perfil", command=save_profile).grid(row=5, columnspan=2)

    def login(self):
        # Ventana para iniciar sesión
        login_win = tk.Toplevel(self.root)
        login_win.title("Iniciar Sesión")

        tk.Label(login_win, text="Correo").grid(row=0, column=0)
        tk.Label(login_win, text="Contraseña (ID)").grid(row=1, column=0)

        email_entry = tk.Entry(login_win)
        password_entry = tk.Entry(login_win, show="*")

        email_entry.grid(row=0, column=1)
        password_entry.grid(row=1, column=1)

        def attempt_login():
            correo = email_entry.get()
            contra = int(password_entry.get())
            if self.estudio.iniciar_sesion(correo, contra):
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            else:
                messagebox.showerror("Error", "Correo o contraseña incorrectos")
            login_win.destroy()

        tk.Button(login_win, text="Iniciar Sesión", command=attempt_login).grid(row=2, columnspan=2)

    def view_events(self):
        # Mostrar próximos eventos
        eventos = self.estudio.calendario.eventos_del_tiempo(7)  # Eventos en los próximos 7 días
        if eventos:
            eventos_text = "\n".join(str(evento) for evento in eventos)
            messagebox.showinfo("Próximos Eventos", eventos_text)
        else:
            messagebox.showinfo("Próximos Eventos", "No hay eventos próximos")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudyAppGUI(root)
    root.mainloop()
