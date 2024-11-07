import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Label, Button, Entry

from app.model.study import Estudio, Calendario


class VistaVerCalendario:
    def __init__(self, root, usuario, callback_volver):
        self.root = root
        self.usuario = usuario
        self.callback_volver = callback_volver
        self.study = Estudio()  # Instancia de Estudio para manejar eventos
        self.calendario = Calendario()  # Instancia de Calendario para manejar eventos

        # Frame principal del calendario
        self.frame = tk.Frame(self.root, bg="#003366")
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Título
        self.titulo = tk.Label(
            self.frame,
            text=f"Calendario de {self.usuario.nombre}",
            font=("Arial", 20, "bold"),
            bg="#003366",
            fg="white"
        )
        self.titulo.pack(pady=20)

        # Etiqueta y entrada para elegir días
        self.frame_dias = tk.Label(self.frame, text="Ver eventos de los próximos X días:", bg="#003366", fg="white")
        self.frame_dias.pack(pady=5)

        self.entrada_dias = tk.Entry(self.frame, font=("Arial", 12))
        self.entrada_dias.pack(pady=5)

        # Botón para ver eventos
        self.btn_ver_eventos = Button(self.frame, text="Ver eventos", command=self.ver_eventos, width=16)  # Reducido el ancho
        self.btn_ver_eventos.pack(pady=10)

        # Botón para agregar evento
        self.btn_agregar_evento = Button(self.frame, text="Agregar evento", command=self.ventana_agregar_evento,
                                         width=16)  # Reducido el ancho
        self.btn_agregar_evento.pack(pady=10)

        # Listbox para mostrar eventos
        self.lista_eventos = tk.Listbox(self.frame, font=("Arial", 12))
        self.lista_eventos.pack(expand=True, fill='both')
        self.lista_eventos.bind("<<ListboxSelect>>", self.mostrar_detalle_evento)

        # Botón para regresar a la vista principal
        self.btn_volver = Button(
            self.frame,
            text="Volver",
            command=self.volver,
            width=16,  # Acorté más el ancho del botón
        )
        self.btn_volver.pack(pady=15)

    def ver_eventos(self):
        try:
            dias = int(self.entrada_dias.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido de días.")
            return

        self.lista_eventos.delete(0, 'end')
        self.eventos_mostrados = self.calendario.eventos_del_tiempo(dias)
        if not self.eventos_mostrados:
            messagebox.showinfo("Sin eventos", "No hay eventos para los próximos días.")
        for i, evento in enumerate(self.eventos_mostrados):
            self.lista_eventos.insert('end', f"{evento.titulo} - {evento.fecha}")

    def mostrar_detalle_evento(self, event):
        seleccion = self.lista_eventos.curselection()
        if seleccion:
            index = seleccion[0]
            evento_seleccionado = self.eventos_mostrados[index]

            ventana_detalle = tk.Toplevel(self.root)  # Cambié self.master por self.root
            ventana_detalle.title("Detalles del Evento")

            Label(ventana_detalle, text=f"Título: {evento_seleccionado.titulo}", font=("Arial", 12)).pack(pady=5)
            Label(ventana_detalle, text=f"Fecha: {evento_seleccionado.fecha}", font=("Arial", 12)).pack(pady=5)
            Label(ventana_detalle, text=f"Detalles: {evento_seleccionado.detalles}", font=("Arial", 12)).pack(pady=5)

    def ventana_agregar_evento(self):
        ventana = tk.Toplevel(self.root)  # Cambié self.master por self.root
        ventana.title("Agregar Evento")

        Label(ventana, text="Título del Evento:", font=("Arial", 12)).pack(pady=5)
        entrada_titulo = Entry(ventana, font=("Arial", 12))
        entrada_titulo.pack(pady=5)

        Label(ventana, text="Año (YYYY):", font=("Arial", 12)).pack(pady=5)
        entrada_year = Entry(ventana, font=("Arial", 12))
        entrada_year.pack(pady=5)

        Label(ventana, text="Mes (MM):", font=("Arial", 12)).pack(pady=5)
        entrada_mes = Entry(ventana, font=("Arial", 12))
        entrada_mes.pack(pady=5)

        Label(ventana, text="Día (DD):", font=("Arial", 12)).pack(pady=5)
        entrada_dia = Entry(ventana, font=("Arial", 12))
        entrada_dia.pack(pady=5)

        Label(ventana, text="Hora (0-23):", font=("Arial", 12)).pack(pady=5)
        entrada_hora = Entry(ventana, font=("Arial", 12))
        entrada_hora.pack(pady=5)

        Label(ventana, text="Detalles:", font=("Arial", 12)).pack(pady=5)
        entrada_detalles = Entry(ventana, font=("Arial", 12))
        entrada_detalles.pack(pady=5)

        Button(ventana, text="Guardar",
               command=lambda: self.guardar_evento(
                   entrada_titulo.get(),
                   entrada_year.get(),
                   entrada_mes.get(),
                   entrada_dia.get(),
                   entrada_hora.get(),
                   entrada_detalles.get()
               )).pack(pady=10)

    def guardar_evento(self, titulo, year, mes, dia, hora, detalles):
        try:
            year = int(year)
            mes = int(mes)
            dia = int(dia)
            hora = int(hora)
        except ValueError:
            messagebox.showerror("Error", "Fecha u hora no válidas.")
            return

        if self.calendario.agregar_evento(titulo, year, mes, dia, hora, detalles=detalles):
            messagebox.showinfo("Éxito", "Evento agregado con éxito")
        else:
            messagebox.showerror("Error", "No se pudo agregar el evento.")

    def volver(self):
        self.frame.pack_forget()
        self.callback_volver()  # Llama la función de callback para volver a la vista principal
