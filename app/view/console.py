from app.model.study import Estudio


class ConsoleView:

    def __init__(self, estudio: Estudio):
        self.estudio: Estudio = estudio

    @staticmethod
    def show_welcome_msg():
        print(f"{"+" * 10}")
        print("Bienvenido a Study App\nEl mejor aliado de la educación")
        print(f"{"+" * 10}")

    @staticmethod
    def show_menu():
        print("\nOPTIONS:")
        print("1. Ver Calendario Personal")
        print("2. Agregar un Evento al Clendario")
        print("3. Crear Grupo de Estudio")
        print("4. Buscar Grupo de Estudio")
        print("5. Agregar un Evento al Grupo de Estudio")
        print("6. Buscar Plan de Estudio")
        print("7. Exit program")
        option = int(input("Enter an option: "))
        while option not in range(1, 8):
            print(">>> ERROR: Invalid option. Try again")
            option = int(input("Enter an option: "))
        return option

    def app_loop(self):
        ConsoleView.show_welcome_msg()
        end_app: bool = False
        while not end_app:
            option: int = ConsoleView.show_menu()
            end_app = self.process_user_option(option)

