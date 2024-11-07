import tkinter as tk
from tkinter import messagebox, ttk
from app.model.study import Examen

class VistaBuscarExamenes:
    def __init__(self, root, estudio, mostrar_vista_anterior):
        self.root = root
        self.estudio = estudio
        self.mostrar_vista_anterior = mostrar_vista_anterior

        # Frame principal
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Título
        self.titulo = tk.Label(self.frame, text="Buscar Exámenes", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=20)

        # Treeview para mostrar exámenes
        self.tree = ttk.Treeview(self.frame, columns=("Materia", "Temática"), show='headings')
        self.tree.heading("Materia", text="Materia")
        self.tree.heading("Temática", text="Temática")
        self.tree.pack(expand=True, fill='both')

        # Cargar exámenes
        self.cargar_examenes()

        # Botón para iniciar examen
        self.btn_iniciar = ttk.Button(self.frame, text="Iniciar Examen", command=self.iniciar_examen)
        self.btn_iniciar.pack(pady=10)

        # Botón para volver
        self.btn_volver = ttk.Button(self.frame, text="Volver", command=self.volver)
        self.btn_volver.pack(pady=10)

    def cargar_examenes(self):
        """Carga los exámenes en el Treeview."""
        for examen in self.estudio.examenes:
            self.tree.insert("", "end", values=(examen.materia, examen.tematica))

    def iniciar_examen(self):
        """Inicia el examen seleccionado."""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un examen primero.")
            return

        item = self.tree.item(seleccion[0])
        materia_examen = item['values'][0]

        # Obtener el examen seleccionado
        examen_seleccionado = next((examen for examen in self.estudio.examenes if examen.materia == materia_examen),
                                   None)

        if examen_seleccionado:
            self.frame.destroy()
            from app.view.vista_buscar_examen import VistaExamen  # Asegúrate de que esta vista exista
            VistaExamen(self.root, examen_seleccionado, self.volver)  # Pasar el examen seleccionado aquí
        else:
            messagebox.showerror("Error", "Examen no encontrado.")

    def volver(self):
        """Vuelve a la vista anterior."""
        self.frame.destroy()
        self.mostrar_vista_anterior()



class VistaExamen:
    def __init__(self, root, examen, callback_volver):
        self.root = root
        self.examen = examen
        self.callback_volver = callback_volver
        self.respuestas = []
        self.pregunta_actual = 0

        # Frame principal
        self.frame = tk.Frame(self.root, bg="#003366")
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Título
        self.titulo = tk.Label(
            self.frame,
            text=f"Examen de {self.examen.materia}",
            font=("Arial", 20, "bold"),
            bg="#003366",
            fg="white"
        )
        self.titulo.pack(pady=20)

        # Pregunta
        self.label_pregunta = tk.Label(self.frame, text="", bg="#003366", fg="white", wraplength=400)
        self.label_pregunta.pack(pady=10)

        # Opciones de respuesta
        self.var_respuesta = tk.StringVar()
        self.opciones = ttk.Combobox(self.frame, textvariable=self.var_respuesta, state="readonly")
        self.opciones.pack(pady=10)

        # Botón Siguiente
        self.btn_siguiente = ttk.Button(self.frame, text="Siguiente", command=self.siguiente_pregunta)
        self.btn_siguiente.pack(pady=10)

        # Cargar la primera pregunta
        self.cargar_pregunta()

    def cargar_pregunta(self):
        """Carga la pregunta actual y sus opciones."""
        if self.pregunta_actual < self.examen.numero_preguntas:
            pregunta = self.examen.preguntas[self.pregunta_actual]
            self.label_pregunta.config(text=pregunta)

            # Aquí puedes definir las opciones de respuesta (puedes personalizarlas)
            # Para este ejemplo, vamos a usar opciones de respuesta ficticias
            self.opciones['values'] = ["Opción A", "Opción B", "Opción C", "Opción D"]  # Ejemplo de opciones
            self.opciones.set("")  # Reiniciar selección
        else:
            self.finalizar_examen()

    def siguiente_pregunta(self):
        """Avanza a la siguiente pregunta."""
        respuesta_seleccionada = self.var_respuesta.get()
        if respuesta_seleccionada == "":
            messagebox.showwarning("Advertencia", "Por favor, selecciona una respuesta.")
            return

        # Guardar la respuesta
        self.respuestas.append(respuesta_seleccionada)

        # Avanzar a la siguiente pregunta
        self.pregunta_actual += 1
        self.cargar_pregunta()

    def finalizar_examen(self):
        """Calcula los resultados y muestra el resumen."""
        numero_buenas, preguntas_malas = self.examen.calcular_resultados(self.respuestas)

        # Mostrar resultados
        resultados = f"Has respondido correctamente {numero_buenas} de {self.examen.numero_preguntas} preguntas.\n"
        if preguntas_malas:
            resultados += "Respuestas incorrectas:\n"
            for pregunta, respuesta_correcta in preguntas_malas.items():
                resultados += f"- {pregunta} (Respuesta correcta: {respuesta_correcta})\n"

        messagebox.showinfo("Resultados del Examen", resultados)

        # Volver a la vista anterior
        self.frame.destroy()
        self.callback_volver()