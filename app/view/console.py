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
        pass

    def agregar_evento(self):
        pass

    def crear_grupo_de_estudio(self):
        print("\n=== CREAR GRUPO DE ESTUDIO ===\n")
        nombre = input("Ingrese el nombre del Grupo: ")
        tematica = input("Ingrese la materia de Estudio: ")
        modalidad = input("Ingrese la modalidad de las Reuniones, es decir, Presencial o Virtual: ")
        horario = int(input("Ingrese la hora de reunión en formato militar: "))
        resultado = self.estudio.registrar_grupo_de_estudio(nombre,tematica, modalidad,horario)
        if resultado:
            print(f"Grupo {nombre} fue creado con Éxito")
        else:
            print(f"No fue posible crear el Grupo {nombre}")


    def buscar_grupo_de_estudio(self):
        print("\n=== BUSCAR GRUPO DE ESTUDIO ===\n")
        tematica: str = input("Ingrese la tematica que desea que tenga el Grupo: ")
        modalidad: str = input("Ingrese la modalidad que desea el Grupo: ")
        horario: int = int(input("Ingrese el horario en el que desea el Grupo: "))
        print(self.estudio.buscar_grupo_de_estudio(tematica, modalidad, horario))

    def agregar_evento_grupo_estudio(self):
        pass

    def buscar_plan_estudio(self):
        pass

    def ingresar_a_grupo_de_estudio(self):
        pass
        print("\n=== INGRESAR A GRUPO DE ESTUDIO ===\n")
        nombre = input("Ingrese el nombre del Grupo de Estudio al que se desea Unir: ")
        self.estudio.registrar_nuevo_miembro(nombre)

    def buscar_examen(self):
        pass