class Evento:

    def __init__(self, titulo: str, fecha: int, duracion: int = 0, ubicacion: str = "", detalles: str = ""):
        self.titulo: str = titulo
        self.fecha: int = fecha
        self.duracion: int = duracion
        self.ubicacion: str = ubicacion
        self.detalles: str = detalles


class Calendario:

    def __init__(self):
        self.eventos: list[Evento] = []

    def verificar_evento(self, titulo: str) -> bool:
        for evento in self.eventos:
            if titulo == self.eventos[evento].titulo:
                return True
        return False

    def agregar_evento(self, titulo: str, fecha: int, duracion: int = 0, ubicacion: str = "", detalles: str = ""):
        self.eventos.append(Evento(titulo, fecha))

    def eventos_del_tiempo(self, tiempo: int):
        pass


class GrupoDeEstudio:

    def __init__(self, nombre: str, tematica: str, modalidad: str, horario: int):
        self.nombre: str = nombre
        self.tematica: str = tematica
        self.modalidad: str = modalidad
        self.horario: int = horario
        self.miembros: list[Usuario] = []


class Usuario:

    def __init__(self, nombre: str, correo: str, id: int, carrera: str, semestre_actual: int):
        self.nombre: str = nombre
        self.correo: str = correo
        self.id: int = id
        self.carrera: str = carrera
        self.semestre_actual: int = semestre_actual
        self.grupos_pertenecientes: list[GrupoDeEstudio] = []

    def pertenece_a_almenos_un_grupo(self) -> bool:
        if len(self.grupos_pertenecientes) == 0:
            return False
        return True


class PlanDeEstudio:

    def __init__(self, materia: str, universidad: str, intensidad_semanal: int):
        self.materia: str = materia
        self.universidad: str = universidad
        self.intensidad_semanal: int = intensidad_semanal


class Estudio:

    def __init__(self, lista_de_estudiantes: list[Usuario],
                 grupos_de_estudio: list[GrupoDeEstudio], planes_de_estudio: list[PlanDeEstudio]):
        self.estudiantes: list[Usuario] = lista_de_estudiantes
        self.grupos_de_estudio: list[GrupoDeEstudio] = grupos_de_estudio
        self.planes_de_estudio: list[PlanDeEstudio] = planes_de_estudio

    def registrar_estudiante(self, nombre: str, id: int, correo: str, carrera: str, semestre_actual: int):
        estudiantes_antes: int = len(self.estudiantes)
        self.estudiantes.append(Usuario(nombre, correo, id, carrera, semestre_actual))
        if estudiantes_antes < len(self.estudiantes):
            return True
        return False

    def iniciar_sesion(self, usuario: int, contra: int) -> bool:
        for estudiante in self.estudiantes:
            if estudiante.id == usuario:
                return True
        return False













