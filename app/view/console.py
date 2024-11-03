from datetime import datetime
from app.model.study import Estudio
from app.model.errors import EntradaInvalidaError, UsuarioNoEncontradoError, GrupoNoEncontradoError, \
    EventoFechaPasadaError


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
        print("8. Salir de la Aplicación")
        while True:
            try:
                option = int(input("Ingrese una Opción: "))
                if option not in range(1, 9):
                    return option
                else:
                    raise EntradaInvalidaError()
            except ValueError:
                print(">>> ERROR: Opción inválida. Intente de nuevo.")

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
            self.exit_app()
            return True

        return False

    @staticmethod
    def exit_app():
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
        except EventoFechaPasadaError as err:
            print(err.mensaje)

    def crear_grupo_de_estudio(self):
        try:
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
            self.estudio.registrar_grupo_de_estudio(nombre, tematica, modalidad, horario)
            print(f"Grupo {nombre} fue creado con Éxito")
        except ValueError:
            print(">>> ERROR: Opción inválida. Intente de nuevo.")

    def buscar_grupo_de_estudio(self):
        try:
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
        except GrupoNoEncontradoError as err:
            print(err.mensaje)

    def agregar_evento_grupo_estudio(self):
        try:
            print("\n=== AGREGAR EVENTO AL GRUPO DE ESTUDIO ===\n")
            nombre_grupo = input("Ingrese el nombre del grupo al que desea agregar un evento: ")
            grupo = next((grupo for grupo in self.estudio.grupos_de_estudio if grupo.nombre == nombre_grupo), None)
            if grupo is None:
                print(f">>> ERROR: No se encontró el grupo {nombre_grupo}.")
                return
            titulo = input("Ingrese el título del evento: ")
            fecha_input = input("Ingrese la fecha y hora del evento (formato YYYY-MM-DD HH:MM): ")
            fecha = datetime.strptime(fecha_input, "%Y-%m-%d %H:%M")
            duracion = int(input("Ingrese la duración en horas: "))
            ubicacion = input("Ingrese la ubicación del evento: ")
            detalles = input("Ingrese los detalles del evento: ")
            grupo.agregar_evento_grupo_de_estudio(self.estudio.calendario, titulo, fecha, duracion,
                                                                           ubicacion, detalles)
            print(f"Evento '{titulo}' agregado con éxito al grupo '{nombre_grupo}'.")
        except GrupoNoEncontradoError as err:
            print(err.mensaje)
        except EventoFechaPasadaError as err:
            print(err.mensaje)

    def buscar_plan_estudio(self):
        print("\n=== BUSCAR PLAN DE ESTUDIO ===\n")
        materia = input("Ingrese la materia que desea buscar: ")
        planes = self.estudio.buscar_plan_de_estudio(materia)
        if planes:
            print("Planes de estudio encontrados:\n")
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
