import tkinter as tk
from tkinter import Button, Label, Listbox, Toplevel, Entry, messagebox
from app.model.study import Estudio, Calendario


class VistaVerCalendario:
    def __init__(self, master, usuario, callback_volver):
        self.crear_interfaz()
        self.master = master
        self.usuario = usuario
        self.callback_volver = callback_volver
        self.study = Estudio()  # Instancia de Estudio para manejar eventos
        self.calendario = Calendario()

        # Definición de los elementos de la interfaz
        self.entrada_dias = None
        self.btn_ver_eventos = None
        self.btn_agregar_evento = None
        self.lista_eventos = None
        self.eventos_mostrados = []  # Atributo para guardar los eventos mostrados actualmente


    def crear_interfaz(self):
        # Frame principal del calendario
        self.frame = tk.Frame(self.master, bg="#003366")
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Título
        Label(
            self.frame,
            text=f"Calendario de {self.usuario.nombre}",
            font=("Arial", 20, "bold"),
            bg="#003366",
            fg="white"
        ).pack(pady=20)

        # Entrada para elegir días
        Label(self.frame, text="Ver eventos de los próximos X días:", bg="#003366", fg="white").pack()
        self.entrada_dias = Entry(self.frame)
        self.entrada_dias.pack()

        # Botón para ver eventos
        self.btn_ver_eventos = Button(self.frame, text="Ver eventos", command=self.ver_eventos)
        self.btn_ver_eventos.pack()

        # Botón para agregar evento
        self.btn_agregar_evento = Button(self.frame, text="Agregar evento", command=self.ventana_agregar_evento)
        self.btn_agregar_evento.pack()

        # Listbox para mostrar eventos y configurar selección de eventos
        self.lista_eventos = Listbox(self.frame)
        self.lista_eventos.pack()
        self.lista_eventos.bind("<<ListboxSelect>>", self.mostrar_detalle_evento)

        # Botón para regresar a la vista principal
        self.btn_volver = Button(
            self.frame,
            text="Volver",
            command=self.volver,
            bg="#005580",
            fg="white",
            width=20
        )
        self.btn_volver.pack(pady=20)

    def ver_eventos(self):
        try:
            dias = int(self.entrada_dias.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido de días.")
            return

        self.lista_eventos.delete(0, 'end')
        self.eventos_mostrados = self.calendario.eventos_del_tiempo(dias)
        for i, evento in enumerate(self.eventos_mostrados):
            self.lista_eventos.insert('end', f"{evento.titulo} - {evento.fecha}")

    def mostrar_detalle_evento(self, event):
        seleccion = self.lista_eventos.curselection()
        if seleccion:
            index = seleccion[0]
            evento_seleccionado = self.eventos_mostrados[index]

            ventana_detalle = Toplevel(self.master)
            ventana_detalle.title("Detalles del Evento")

            Label(ventana_detalle, text=f"Título: {evento_seleccionado.titulo}").pack()
            Label(ventana_detalle, text=f"Fecha: {evento_seleccionado.fecha}").pack()
            Label(ventana_detalle, text=f"Detalles: {evento_seleccionado.detalles}").pack()

    def ventana_agregar_evento(self):
        ventana = Toplevel(self.master)
        ventana.title("Agregar Evento")

        Label(ventana, text="Título del Evento:").pack()
        entrada_titulo = Entry(ventana)
        entrada_titulo.pack()

        Label(ventana, text="Año (YYYY):").pack()
        entrada_year = Entry(ventana)
        entrada_year.pack()

        Label(ventana, text="Mes (MM):").pack()
        entrada_mes = Entry(ventana)
        entrada_mes.pack()

        Label(ventana, text="Día (DD):").pack()
        entrada_dia = Entry(ventana)
        entrada_dia.pack()

        Label(ventana, text="Hora (0-23):").pack()
        entrada_hora = Entry(ventana)
        entrada_hora.pack()

        Label(ventana, text="Detalles:").pack()
        entrada_detalles = Entry(ventana)
        entrada_detalles.pack()

        Button(ventana, text="Guardar",
               command=lambda: self.guardar_evento(
                   entrada_titulo.get(),
                   entrada_year.get(),
                   entrada_mes.get(),
                   entrada_dia.get(),
                   entrada_hora.get(),
                   entrada_detalles.get()
               )).pack()

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
            messagebox.showinfo("Éxito", "Evento agregado correctamente.")
            self.ver_eventos()
        else:
            messagebox.showerror("Error", "Error al agregar el evento.")

    def volver(self):
        self.frame.pack_forget()
        self.callback_volver()
