from app.model.study import Estudio
from app.view.console import ConsoleView


def main():
    estudio: Estudio = Estudio()
    ui: ConsoleView = ConsoleView(estudio)
    ui.app_loop()


if __name__ == "__main__":
    main()
