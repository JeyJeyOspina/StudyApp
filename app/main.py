import tkinter as tk
from app.view.vista_inicial import VistaInicial


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendario de Eventos")
        self.root.geometry("400x300")

        # Inicializar la vista inicial
        self.vista_inicial = VistaInicial(self.root, self.cambiar_a_vista_registro)

    def cambiar_a_vista_registro(self):
        self.vista_inicial.destroy()  # Destruir la vista inicial
        from vista_registro import VistaRegistro  # Importar la vista de registro
        self.vista_registro = VistaRegistro(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()