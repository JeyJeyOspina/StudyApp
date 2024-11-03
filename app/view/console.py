from datetime import datetime
from app.model.study import Estudio
#from app.model.errors import EntradaInvalidaError, UsuarioNoEncontradoError, GrupoNoEncontradoError


class ConsoleView:

    def __init__(self, estudio: Estudio):
        self.estudio: Estudio = estudio

    @staticmethod
    def show_welcome_msg():
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Bienvenido a Study App\nEl mejor aliado de la educación")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    @staticmethod
    def show_menu():
        print("\nMENÚ:")
        print("1. Ver Calendario Personal")
        print("2. Agregar un Evento al Clendario")
        print("3. Crear Grupo de Estudio")
        print("4. Buscar Grupo de Estudio")
        print("5. Agregar un Evento al Grupo de Estudio")
        print("6. Buscar Plan de Estudio")
        print("7. Ingresar Grupo de Estudio")
        print("8. Buscar Examen")
        print("9. Salir de la Aplicación")
        option = int(input("Ingrese una Opción: "))
        while option not in range(1, 10):
            print(">>> ERROR: Invalid option. Try again")
            option = int(input("Enter an option: "))
        return option

    def app_loop(self):
        ConsoleView.show_welcome_msg()
        end_app: bool = False
        while not end_app:
            option: int = ConsoleView.show_menu()
            end_app = self.process_user_option(option)

    def process_user_option(self, option: int) -> bool:
        if option == 1:
            self.ver_calendario()
        elif option == 2:
            self.agregar_evento()
        elif option == 3:
            self.crear_grupo_de_estudio()
        elif option == 4:
            self.buscar_grupo_de_estudio()
        elif option == 5:
            self.agregar_evento_grupo_estudio()
        elif option == 6:
            self.buscar_plan_estudio()
        elif option == 7:
            self.ingresar_a_grupo_de_estudio()
        elif option == 8:
            self.buscar_examen()
        elif option == 9:
            self.exit_app()
            return True

        return False

    def exit_app(self):
        print("++++++++++++++++++++++++++++++++")
        print("+++ Saliste de la Aplicación +++")
        print("++++++++++++++++++++++++++++++++")

    def ver_calendario(self):
        print("\n=== CALENDARIO PERSONAL ===\n")
        dias = int(input("Ingrese el número de días para ver eventos próximos: "))
        eventos = self.estudio.calendario.eventos_del_tiempo(dias)

        if eventos:
            print("\n=== Eventos próximos ===\n")
            for evento in eventos:
                print(f"Título: {evento.titulo}, Fecha: {evento.fecha}, Duración: {evento.duracion} horas\n")
                print(f"Ubicación: {evento.ubicacion}, Detalles: {evento.detalles}")
                print("--------------------------------------------------")
        else:
            print("No hay eventos agendados en los próximos días especificados.")

    def agregar_evento(self):
        print("\n=== AGREGAR EVENTO ===\n")
        titulo = input("Ingrese el título del evento: ")
        fecha_input = input("Ingrese la fecha y hora del evento (formato YYYY-MM-DD HH:MM): ")
        try:
            fecha = datetime.strptime(fecha_input, "%Y-%m-%d %H:%M")
            duracion = int(input("Ingrese la duración en horas: "))
            ubicacion = input("Ingrese la ubicación del evento: ")
            detalles = input("Ingrese los detalles del evento: ")
            resultado = self.estudio.calendario.agregar_evento(titulo, fecha, duracion, ubicacion, detalles)
            if resultado:
                print(f"Evento '{titulo}' agregado con éxito.")
            else:
                print(f"No se pudo agregar el evento '{titulo}'.")
        except ValueError:
            print(">>> ERROR: Formato de fecha/hora inválido. Intente de nuevo.")

    def crear_grupo_de_estudio(self):
        print("\n=== CREAR GRUPO DE ESTUDIO ===\n")
        nombre = input("Ingrese el nombre del Grupo: ")
        tematica = input("Ingrese la materia de Estudio: ")
        while True:
            modalidad = input("Ingrese la modalidad de las Reuniones (Presencial o Virtual): ")
            if modalidad.lower() in ["presencial", "virtual"]:
                modalidad = modalidad.capitalize()
                break
            else:
                print(">>> ERROR: Modalidad no válida. Por favor, ingrese 'Presencial' o 'Virtual'.")

        while True:
            horario_input = input("Ingrese el horario en el que desea el Grupo (formato HH:MM): ")
            try:
                horario = datetime.strptime(horario_input, "%H:%M").time()
                break
            except ValueError:
                print("Formato de hora inválido. Por favor, intente de nuevo.")
        resultado = self.estudio.registrar_grupo_de_estudio(nombre, tematica, modalidad, horario)
        if resultado:
            print(f"Grupo {nombre} fue creado con Éxito")
        else:
            print(f"No fue posible crear el Grupo {nombre}")

    def buscar_grupo_de_estudio(self):
        print("=== BUSCAR GRUPO DE ESTUDIO ===")
        tematica = input("Ingrese la temática que desea que tenga el Grupo: ")
        while True:
            modalidad = input("Ingrese la modalidad de las Reuniones (Presencial o Virtual): ")
            if modalidad.lower() in ["presencial", "virtual"]:
                modalidad = modalidad.capitalize()
                break
            else:
                print(">>> ERROR: Modalidad no válida. Por favor, ingrese 'Presencial' o 'Virtual'.")

        while True:
            horario_input = input("Ingrese el horario en el que desea el Grupo (formato HH:MM): ")
            try:
                horario = datetime.strptime(horario_input, "%H:%M").time()
                break
            except ValueError:
                print("Formato de hora inválido. Por favor, intente de nuevo.")

        grupos_encontrados = self.estudio.buscar_grupo_de_estudio(tematica, modalidad, horario)
        print(grupos_encontrados)

    def agregar_evento_grupo_estudio(self):
        print("\n=== AGREGAR EVENTO AL GRUPO DE ESTUDIO ===\n")
        nombre_grupo = input("Ingrese el nombre del grupo al que desea agregar un evento: ")
        tematica = input("Ingrese la temática del grupo: ")
        modalidad = input("Ingrese la modalidad del grupo (Presencial o Virtual): ")
        horario_input = input("Ingrese el horario del grupo (formato HH:MM): ")

        try:
            horario = datetime.strptime(horario_input, "%H:%M").time()
            grupo = self.estudio.buscar_grupo_de_estudio(tematica, modalidad, horario)
        except ValueError:
            print(">>> ERROR: Formato de fecha/hora inválido. Intente de nuevo.")

    def buscar_plan_estudio(self):
        print("\n=== BUSCAR PLAN DE ESTUDIO ===\n")
        materia = input("Ingrese la materia que desea buscar: ")
        planes = self.estudio.buscar_plan_de_estudio(materia)
        if planes:
            for plan in planes:
                print(plan)
        else:
            print(f"No se encontraron planes de estudio para la materia '{materia}'.")

    def ingresar_a_grupo_de_estudio(self):
        print("\n=== INGRESAR A GRUPO DE ESTUDIO ===\n")
        nombre_grupo = input("Ingrese el nombre del grupo al que desea ingresar: ")
        usuario_id = int(input("Ingrese su ID: "))
        usuario = None
        for estudiante in self.estudio.estudiantes:
            if estudiante.id == usuario_id:
                usuario = estudiante
                break
        if usuario:
            resultado = self.estudio.registrar_nuevo_miembro(nombre_grupo, usuario)
            if resultado:
                print(f"{usuario.nombre} fue agregado al grupo '{nombre_grupo}' con éxito.")
            else:
                print(f"No fue posible ingresar al grupo '{nombre_grupo}'. El usuario ya está en el grupo.")
        else:
            print(f"Usuario con ID '{usuario_id}' no encontrado.")
    def buscar_examen(self):
        pass