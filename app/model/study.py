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
                break
        return False

    def agregar_evento(self, titulo: str, fecha: int, duracion: int = "", ubicacion: str = "", detalles: str = ""):
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
        self.semestre_actual = int = semestre_actual
        self.grupos_pertenecientes: list[GrupoDeEstudio] = []

    def pertenece_a_almenos_un_grupo(self) -> bool:
        if self.grupos_pertenecientes == None:
            return False
        return True















