from datetime import datetime, timedelta, time


class Evento:

    def __init__(self, titulo: str, fecha: datetime, duracion: int = 0, ubicacion: str = "", detalles: str = ""):
        self.titulo: str = titulo
        self.fecha: datetime = fecha
        self.duracion: int = duracion
        self.ubicacion: str = ubicacion
        self.detalles: str = detalles

    def __str__(self):
        return (f"Evento: {self.titulo}, Fecha: {self.fecha}, "
                f"Duración: {self.duracion} horas, Ubicación: {self.ubicacion}, "
                f"Detalles: {self.detalles}")


class Calendario:

    def __init__(self):
        self.eventos: list[Evento] = []

    def verificar_evento(self, titulo: str) -> bool:
        for evento in self.eventos:
            if evento.titulo == titulo:
                return True
        return False

    def agregar_evento(self, titulo: str, year: int, mes: int, dia: int, hora: int = 0, duracion: int = 1,
                       ubicacion: str = "", detalles: str = "") -> bool:
        fecha: datetime = datetime(year, mes, dia, hora)
        nuevo_evento = Evento(titulo, fecha, duracion, ubicacion, detalles)
        if fecha >= datetime.now():
            self.eventos.append(nuevo_evento)
            return True
        return False

    def eventos_del_tiempo(self, dias: int) -> list[Evento]:
        ahora = datetime.now()
        eventos_en_tiempo = []
        for evento in self.eventos:
            if ahora <= evento.fecha <= ahora + timedelta(days=dias):
                eventos_en_tiempo.append(evento)
        return eventos_en_tiempo if eventos_en_tiempo else ["No hay eventos próximos en el periodo indicado."]
        limite = ahora + timedelta(days=dias)
        eventos_proximos = [evento for evento in self.eventos if ahora <= evento.fecha < limite]
        return eventos_proximos


class GrupoDeEstudio:

    def __init__(self, nombre: str, tematica: str, modalidad: str, horario: time):
        self.nombre: str = nombre
        self.tematica: str = tematica
        self.modalidad: str = modalidad
        self.horario: time = horario
        self.miembros: list[Usuario] = []

    def agregar_evento_grupo_de_estudio(self, calendario: Calendario, titulo: str, fecha: datetime, duracion: int = 1,
                                        ubicacion: str = "", detalles: str = "") -> bool:
        if fecha < datetime.now():
            return False

        evento_agregado = calendario.agregar_evento(titulo, fecha, duracion, ubicacion, detalles)
        if evento_agregado:
            return True
        else:
            return False

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

class Examen:

    def __init__(self, materia: str, tematica: str, numero_preguntas: int, preguntas: list[str],
                 respuestas: list[str]):

        self.materia: str = materia
        self.tematica: str = tematica
        self.numero_preguntas: int = numero_preguntas
        self.preguntas: list[str] = preguntas
        self.respuestas: list[str] = respuestas

    def calcular_resultados(self, respuestas: list[str]):

        numero_buenas: int = 0
        preguntas_malas_con_respuestas_correctas: dict[str, str] = {}

        for respuesta in range(self.numero_preguntas):
            if respuestas[respuesta].lower() == self.respuestas[respuesta].lower():
                numero_buenas += 1
            else:
                preguntas_malas_con_respuestas_correctas[self.preguntas[respuesta]] = self.respuestas[respuesta]

        return numero_buenas, preguntas_malas_con_respuestas_correctas

class Estudio:

    def __init__(self,
                 lista_de_estudiantes: list[Usuario] = None,
                 grupos_de_estudio: list[GrupoDeEstudio] = None,
                 planes_de_estudio: list[PlanDeEstudio] = None):
        self.estudiantes: list[Usuario] = lista_de_estudiantes if lista_de_estudiantes is not None else []
        self.grupos_de_estudio: list[GrupoDeEstudio] = grupos_de_estudio if grupos_de_estudio is not None else []
        self.planes_de_estudio: list[PlanDeEstudio] = planes_de_estudio if planes_de_estudio is None else []
        self.calendario: Calendario = Calendario()

    def registrar_estudiante(self, nombre: str, id: int, correo: str, carrera: str, semestre_actual: int):
        estudiantes_antes: int = len(self.estudiantes)
        self.estudiantes.append(Usuario(nombre, correo, id, carrera, semestre_actual))
        if estudiantes_antes < len(self.estudiantes):
            return True
        return False

    def iniciar_sesion(self, correo: str, contra: int) -> bool:
        for estudiante in self.estudiantes:
            if estudiante.correo == correo and estudiante.id == contra:
                return True
        return False

    def registrar_grupo_de_estudio(self, nombre: str, tematica: str, modalidad: str, horario: time) -> bool:
        grupos_antes: int = len(self.grupos_de_estudio)
        self.grupos_de_estudio.append(GrupoDeEstudio(nombre, tematica, modalidad, horario))
        if grupos_antes < len(self.grupos_de_estudio):
            return True
        return False

    def buscar_grupo_de_estudio(self, tematica: str, modalidad: str, horario: time) -> GrupoDeEstudio | str:
        for grupo in self.grupos_de_estudio:
            if grupo.tematica == tematica and grupo.modalidad == modalidad and grupo.horario == horario:
                return grupo
        return (f"No hay grupos disponibles con tematica de {tematica}, "
                f"modalidad {modalidad} ni con horario {horario}")

    def buscar_plan_de_estudio(self, materia: str) -> list[PlanDeEstudio]:
        planes_por_materia: list[PlanDeEstudio] = []
        for plan_de_estudio in self.planes_de_estudio:
            if plan_de_estudio.materia == materia:
                planes_por_materia.append(plan_de_estudio)
        return planes_por_materia

    def registrar_nuevo_miembro(self, nombre: str, estudiante: Usuario) -> bool:
        for grupo in self.grupos_de_estudio:
            if grupo.nombre == nombre:
                if estudiante in grupo.miembros:
                    return False
                grupo.miembros.append(estudiante)
                return True
        return False

    def registrar_grupo_a_estudiante(self, estudiante: Usuario, nombre_grupo: str) -> bool:
        for grupo in self.grupos_de_estudio:
            if grupo.nombre == nombre_grupo:
                if estudiante not in grupo.miembros:
                    grupo.miembros.append(estudiante)
                    estudiante.grupos_pertenecientes.append(grupo)
                    return True
                else:
                    return False
        return False

    def plan_de_estudio_universidad(self, materia: str, universidad: str) -> PlanDeEstudio | None:
        ed = self.buscar_plan_de_estudio(materia)
        for plan_de_estudio in ed:
            if plan_de_estudio.universidad == universidad:
                return plan_de_estudio
        return None
