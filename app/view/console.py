from datetime import datetime, time

from app.model.study import Estudio


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
        option = int(input("Ingrese una Opción: "))
        while option not in range(1, 9):
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
            self.exit_app()
            return True

        return False

    @staticmethod
    def exit_app(self):
        print("++++++++++++++++++++++++++++++++")
        print("+++ Saliste de la Aplicación +++")
        print("++++++++++++++++++++++++++++++++")

    def ver_calendario(self):
        pass

    def agregar_evento(self):
        pass

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
        pass

    def buscar_plan_estudio(self):
        pass

    def ingresar_a_grupo_de_estudio(self):
        pass
