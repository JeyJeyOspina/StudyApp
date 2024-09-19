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
            if evento.titulo == titulo:
                return True
        return False

    def agregar_evento(self, titulo: str, fecha: int, duracion: int = 0, ubicacion: str = "", detalles: str = ""):
        self.eventos.append(Evento(titulo, fecha, duracion, ubicacion, detalles))

    def eventos_del_tiempo(self, tiempo: int):
        pass


class GrupoDeEstudio:

    def __init__(self, nombre: str, tematica: str, modalidad: str, horario: int):
        self.nombre: str = nombre
        self.tematica: str = tematica
        self.modalidad: str = modalidad
        self.horario: int = horario
        self.miembros: list[Usuario] = []

    def __str__(self):
        return (f"Nombre: {self.nombre}, Tematica: {self.tematica}, "
                f"Modalidad: {self.modalidad}, Horario: {self.horario}")



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

    def __init__(self, lista_de_estudiantes: list[Usuario] = None,
                 grupos_de_estudio: list[GrupoDeEstudio] = None, planes_de_estudio: list[PlanDeEstudio] = None):
        self.estudiantes: list[Usuario] = lista_de_estudiantes if lista_de_estudiantes is not None else []
        self.grupos_de_estudio: list[GrupoDeEstudio] = grupos_de_estudio if grupos_de_estudio is not None else []
        self.planes_de_estudio: list[PlanDeEstudio] = planes_de_estudio if planes_de_estudio is None else []

    def registrar_estudiante(self, nombre: str, id: int, correo: str, carrera: str, semestre_actual: int):
        estudiantes_antes: int = len(self.estudiantes)
        self.estudiantes.append(Usuario(nombre, correo, id, carrera, semestre_actual))
        if estudiantes_antes < len(self.estudiantes):
            return True
        return False

    def iniciar_sesion(self, correo: int, contra: int) -> bool:
        for estudiante in self.estudiantes:
            if estudiante.correo == correo and estudiante.id == contra:
                return True
        return False

    # Hace parte del R4 que aún no tiene la descomposición corregida
    def registrar_grupo_de_estudio(self, nombre: str, tematica: str, modalidad: str, horario: int) -> bool  :
        grupos_antes: int = len(self.grupos_de_estudio)
        self.grupos_de_estudio.append(GrupoDeEstudio(nombre, tematica, modalidad, horario))
        if grupos_antes < len(self.grupos_de_estudio):
            return True
        return False

    def buscar_grupo_de_estudio(self, tematica: str, modalidad: str, horario: int) -> list[str] | str:
        grupos_encontrados: list[GrupoDeEstudio] = []
        for grupo in self.grupos_de_estudio:
            if grupo.tematica == tematica and  grupo.modalidad == modalidad and grupo.horario == horario:
                grupos_encontrados.append(grupo)
        if len(grupos_encontrados) != 0:
            return [str(grupo) for grupo in grupos_encontrados]
        else:
            return (f"No hay grupos disponibles con tematica de {tematica}, "
                    f"modalidad {modalidad} ni con horario {horario}")




    def buscar_plan_de_estudio(self, materia: str) -> list[PlanDeEstudio]:
        planes_por_materia: list[PlanDeEstudio] = []
        for plan_de_estudio in self.planes_de_estudio:
            if plan_de_estudio.materia == materia:
                planes_por_materia.append(plan_de_estudio)
        return planes_por_materia

    def agregar_nuevo_miembro(self, nombre: str, estudiante: Usuario) -> bool:
        for grupo in self.grupos_de_estudio:
            if grupo.nombre == nombre:
                miembros_antes = len(grupo.miembros)
                grupo.miembros.append(estudiante)
                miembros_actual = len(grupo.miembros)
                if miembros_antes < miembros_actual:
                    return True
                return False



"""    def plan_de_estudio_universidad(self, materia: str, universidad: str) -> PlanDeEstudio:
        ed = Estudio().buscar_plan_de_estudio(materia)
        for plan_de_estudio in ed:
            if plan_de_estudio.universidad == universidad:
                return plan_de_estudio"""