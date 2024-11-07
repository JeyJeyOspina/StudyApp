import json
import os
from datetime import datetime, timedelta, time
from typing import List, Dict, Optional

class Evento:
    def __init__(self, titulo: str, year: int, mes: int, dia: int, hora: int, duracion: int = 0,
                 ubicacion: str = "", detalles: str = ""):
        self.titulo: str = titulo
        self.fecha: datetime = datetime(year, mes, dia, hora)
        self.duracion: int = duracion
        self.ubicacion: str = ubicacion
        self.detalles: str = detalles

    def __str__(self):
        return (f"Evento: {self.titulo}, Fecha: {self.fecha}, "
                f"Duración: {self.duracion} horas, Ubicación: {self.ubicacion}, "
                f"Detalles: {self.detalles}")

class Calendario:
    def __init__(self):
        self.eventos: List[Evento] = []

    def verificar_evento(self, titulo: str) -> bool:
        return any(evento.titulo == titulo for evento in self.eventos)

    def agregar_evento(self, titulo: str, year: int, mes: int, dia: int, hora: int = 0, duracion: int = 1,
                       ubicacion: str = "", detalles: str = "") -> bool:
        fecha: datetime = datetime(year, mes, dia, hora)
        if fecha >= datetime.now():
            nuevo_evento = Evento(titulo, year, mes, dia, hora, duracion, ubicacion, detalles)
            self.eventos.append(nuevo_evento)
            return True
        return False

    def eventos_del_tiempo(self, dias: int) -> List[Evento]:
        ahora = datetime.now()
        limite = ahora + timedelta(days=dias)
        return [evento for evento in self.eventos if ahora <= evento.fecha < limite]

class GrupoDeEstudio:
    def __init__(self, nombre: str, tematica: str, modalidad: str, horario: time):
        self.nombre: str = nombre
        self.tematica: str = tematica
        self.modalidad: str = modalidad
        self.horario: time = horario
        self.miembros: List['Usuario'] = []

    def agregar_evento_grupo_de_estudio(self, calendario: Calendario, titulo: str, year: int, mes: int, dia: int,
                                        hora: int = 0, duracion: int = 0,
                                        ubicacion: str = "", detalles: str = "") -> bool:
        fecha: datetime = datetime(year, mes, dia, hora)
        if fecha < datetime.now():
            return False
        return calendario.agregar_evento(titulo, year, mes, dia, hora, duracion, ubicacion, detalles)

    def __str__(self):
        return (f"Nombre: { self.nombre}, Tematica: {self.tematica}, "
                f"Modalidad: {self.modalidad}, Horario: {self.horario}")

class Usuario:
    def __init__(self, nombre: str, correo: str, id: int, carrera: str, semestre_actual: int):
        self.nombre: str = nombre
        self.correo: str = correo
        self.id: int = id
        self.carrera: str = carrera
        self.semestre_actual: int = semestre_actual
        self.grupos_pertenecientes: List[GrupoDeEstudio] = []
        self.calendario: List[Calendario] = []

    def pertenece_a_almenos_un_grupo(self) -> bool:
        return len(self.grupos_pertenecientes) > 0

    def __str__(self):
        return f"Nombre: {self.nombre.upper()}, Carrera: {self.carrera.upper()} , Usuario: {self.id} "

class PlanDeEstudio:
    def __init__(self, materia: str, universidad: str, intensidad_semanal: int):
        self.materia: str = materia
        self.universidad: str = universidad
        self.intensidad_semanal: int = intensidad_semanal

class Examen:
    def __init__(self, materia: str, tematica: str, numero_preguntas: int, preguntas: List[str],
                 respuestas: List[str]):
        self.materia: str = materia
        self.tematica: str = tematica
        self.numero_preguntas: int = numero_preguntas
        self.preguntas: List[str] = preguntas
        self.respuestas: List[str] = respuestas

    def calcular_resultados(self, respuestas: List[str]) -> tuple:
        numero_buenas: int = 0
        preguntas_malas_con_respuestas_correctas: Dict[str, str] = {}

        for respuesta in range(self.numero_preguntas):
            if respuestas[respuesta].lower() == self.respuestas[respuesta].lower():
                numero_buenas += 1
            else:
                preguntas_malas_con_respuestas_correctas[self.preguntas[respuesta]] = self.respuestas[respuesta]

        return numero_buenas, preguntas_malas_con_respuestas_correctas

    @staticmethod
    def crear_examen_ejemplo() -> 'Examen':
        preguntas = [
            "¿Cuál es la capital de Francia?",
            "¿Cuánto es 2 + 2?",
            "¿Cuál es el océano más grande del mundo?",
            "¿Quién escribió 'Cien años de soledad'?",
            "¿Cuál es la fórmula química del agua?"
        ]
        respuestas = [
            "París",
            "4",
            "Pacífico",
            "Gabriel García Márquez",
            "H2O"
        ]
        return Examen("Geografía", "General", len(preguntas), preguntas, respuestas)

class Estudio:
    _instancia: "Estudio" = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if not self._inicializado:
            self.estudiantes: List[Usuario] = []
            self.grupos_de_estudio: List[GrupoDeEstudio] = []
            self.planes_de_estudio: List[PlanDeEstudio] = []
            self.calendario: Calendario = Calendario()
            self.examenes: List[Examen] = []
            self.ruta_datos = os.path.join('datos', 'datos_estudio.json')
            os.makedirs(os.path.dirname(self.ruta_datos), exist_ok=True)
            self.cargar_datos()
            self.cargar_examenes()
            self.examenes.append(Examen.crear_examen_ejemplo())
            self.guardar_datos()
            self._inicializado = True

    def guardar_datos(self):
        """Guardamos todos los datos en un archivo JSON"""
        datos = {
            'estudiantes': [
                {
                    'nombre': est.nombre,
                    'correo': est.correo,
                    'id': est.id,
                    'carrera': est.carrera,
                    'semestre_actual': est.semestre_actual,
                    'grupos_pertenecientes': [grupo.nombre for grupo in est.grupos_pertenecientes]
                }
                for est in self.estudiantes
            ],
            'grupos_de_estudio': [
                {
                    'nombre': grupo.nombre,
                    'tematica': grupo.tematica,
                    'modalidad': grupo.modalidad,
                    'horario': grupo.horario.strftime("%H:%M:%S"),
                    'miembros': [miembro.correo for miembro in grupo.miembros]
                }
                for grupo in self.grupos_de_estudio
            ],
            'planes_de_estudio': [
                {
                    'materia': plan.materia,
                    'universidad': plan.universidad,
                    'intensidad_semanal': plan.intensidad_semanal
                }
                for plan in self.planes_de_estudio
            ],
            'calendario': {
                'eventos': [
                    {
                        'titulo': evento.titulo,
                        'fecha': evento.fecha.strftime("%Y-%m-%d %H:%M:%S"),
                        'duracion': evento.duracion,
                        'ubicacion': evento.ubicacion,
                        'detalles': evento.detalles
                    }
                    for evento in self.calendario.eventos
                ]
            },
            'examenes': [
                {
                    'materia': examen.materia,
                    'tematica': examen.tematica,
                    'numero_preguntas': examen.numero_preguntas,
                    'preguntas': examen.preguntas,
                    'respuestas': examen.respuestas
                }
                for examen in self.examenes
            ]
        }

        try:
            with open(self.ruta_datos, 'w') as archivo:
                json.dump(datos, archivo, indent=4)
        except IOError as e:
            print(f"Error al guardar datos: {e}")

    def cargar_datos(self):
        """Cargamos todos los datos desde el archivo JSON"""
        if not os.path.exists(self.ruta_datos):
            return

        try:
            with open(self.ruta_datos, 'r') as archivo:
                datos = json.load(archivo)

            # Cargar estudiantes (primera pasada sin grupos)
            estudiantes_temp = {}
            for est_data in datos.get('estudiantes', []):
                estudiante = Usuario(
                    est_data['nombre'],
                    est_data['correo'],
                    est_data['id'],
                    est_data['carrera'],
                    est_data['semestre_actual']
                )
                self.estudiantes.append(estudiante)
                estudiantes_temp[est_data['correo']] = estudiante

            # Cargar grupos de estudio
            grupos_temp = {}
            for grupo_data in datos.get('grupos_de_estudio', []):
                horario = datetime.strptime(grupo_data['horario'], "%H:%M:%S").time()
                grupo = GrupoDeEstudio(
                    grupo_data['nombre'],
                    grupo_data['tematica'],
                    grupo_data['modalidad'],
                    horario
                )
                # Agregar miembros al grupo
                for correo_miembro in grupo_data['miembros']:
                    if correo_miembro in estudiantes_temp:
                        grupo.miembros.append(estudiantes_temp[correo_miembro])

                self.grupos_de_estudio.append(grupo)
                grupos_temp[grupo_data['nombre']] = grupo

            # Segunda pasada para vincular estudiantes con grupos
            for est_data in datos.get('estudiantes', []):
                estudiante = estudiantes_temp[est_data['correo']]
                for nombre_grupo in est_data['grupos_pertenecientes']:
                    if nombre_grupo in grupos_temp:
                        estudiante.grupos_pertenecientes.append(grupos_temp[nombre_grupo])

            # Cargar planes de estudio
            for plan_data in datos.get('planes_de_estudio', []):
                plan = PlanDeEstudio(
                    plan_data['materia'],
                    plan_data['universidad'],
                    plan_data['intensidad_semanal']
                )
                self.planes_de_estudio.append(plan)

            # Cargar calendario
            for evento_data in datos.get('calendario', {}).get('eventos', []):
                fecha = datetime.strptime(evento_data['fecha'], "%Y-%m-%d %H:%M:%S")
                evento = Evento(
                    evento_data['titulo'],
                    fecha.year,
                    fecha.month,
                    fecha.day,
                    fecha.hour,
                    evento_data['duracion'],
                    evento_data['ubicacion'],
                    evento_data['detalles']
                )
                self.calendario.eventos.append(evento)

        except IOError as e:
            print(f"Error al cargar datos: {e}")

    def cargar_examenes(self):
        """Cargamos todos los exámenes desde el archivo JSON"""
        if not os.path.exists(self.ruta_datos):
            return

        try:
            with open(self.ruta_datos, 'r') as archivo:
                datos = json.load(archivo)

            # Cargar exámenes
            for examen_data in datos.get('examenes', []):
                examen = Examen(
                    examen_data['materia'],
                    examen_data['tematica'],
                    examen_data['numero_preguntas'],  # Corrección aquí
                    examen_data['preguntas'],
                    examen_data['respuestas']
                )
                self.examenes.append(examen)

        except IOError as e:
            print(f"Error al cargar datos de exámenes: {e}")

    def agregar_examen(self, examen: Examen):
        self.examenes.append(examen)
        self.guardar_datos()

    def registrar_estudiante(self, nombre: str, correo: str, id: int, carrera: str, semestre_actual: int) -> bool:
        estudiantes_antes = len(self.estudiantes)
        nuevo_estudiante = Usuario(nombre, correo, id, carrera, semestre_actual)
        self.estudiantes.append(nuevo_estudiante)
        if estudiantes_antes < len(self.estudiantes):
            self.guardar_datos()
            return True
        return False

    def iniciar_sesion(self, correo: str, clave: int) -> Optional[Usuario]:
        for estudiante in self.estudiantes:
            if estudiante.correo == correo and estudiante.id == clave:
                return estudiante
        return None

    def registrar_grupo_de_estudio(self, nombre: str, tematica: str, modalidad: str, horario: time) -> bool:
        grupos_antes = len(self.grupos_de_estudio)
        nuevo_grupo = GrupoDeEstudio(nombre, tematica, modalidad, horario)
        self.grupos_de_estudio.append(nuevo_grupo)
        if grupos_antes < len(self.grupos_de_estudio):
            self.guardar_datos()
            return True
        return False

    def buscar_grupo_de_estudio(self, tematica: str, modalidad: str, horario: time) -> Optional[GrupoDeEstudio]:
        for grupo in self.grupos_de_estudio:
            if grupo.tematica == tematica and grupo.modalidad == modalidad and grupo.horario == horario:
                return grupo
        return None

    def buscar_plan_de_estudio(self, materia: str) -> List[PlanDeEstudio]:
        return [plan for plan in self.planes_de_estudio if plan.materia == materia]

    def registrar_nuevo_miembro(self, nombre_grupo: str, estudiante: Usuario) -> bool:
        for grupo in self.grupos_de_estudio:
            if grupo.nombre == nombre_grupo:
                if estudiante not in grupo.miembros:
                    grupo.miembros.append(estudiante)
                    self.guardar_datos()
                    return True
                return False
        return False

    def registrar_grupo_a_estudiante(self, estudiante: Usuario, nombre_grupo: str) -> bool:
        for grupo in self.grupos_de_estudio:
            if grupo.nombre == nombre_grupo:
                if estudiante not in grupo.miembros:
                    grupo.miembros.append(estudiante)
                    estudiante.grupos_pertenecientes.append(grupo)
                    self.guardar_datos()
                    return True
                return False
        return False

    def plan_de_estudio_universidad(self, materia: str, universidad: str) -> Optional[PlanDeEstudio]:
        for plan_de_estudio in self.planes_de_estudio:
            if plan_de_estudio.materia == materia and plan_de_estudio.universidad == universidad:
                return plan_de_estudio
        return None


#Aqui esta el Código sin la implementación de la persistencia, lo deje para facilidad de estudio en cuanto a los cambios
"""class Estudio:

    def __init__(self,
                 lista_de_estudiantes: list[Usuario] = None,
                 grupos_de_estudio: list[GrupoDeEstudio] = None,
                 planes_de_estudio: list[PlanDeEstudio] = None):

        self.estudiantes: list[Usuario] = lista_de_estudiantes if lista_de_estudiantes is not None else []
        self.grupos_de_estudio: list[GrupoDeEstudio] = grupos_de_estudio if grupos_de_estudio is not None else []
        self.planes_de_estudio: list[PlanDeEstudio] = planes_de_estudio if planes_de_estudio is None else []
        self.calendario: Calendario = Calendario()

    def registrar_estudiante(self, nombre: str,correo: str, id: int,  carrera: str, semestre_actual: int):
        estudiantes_antes: int = len(self.estudiantes)
        self.estudiantes.append(Usuario(nombre, correo, id, carrera, semestre_actual))
        if estudiantes_antes < len(self.estudiantes):
            return True
        return False

    def iniciar_sesion(self, correo: str, clave: int) -> bool:
        for estudiante in self.estudiantes:
            if estudiante.correo == correo and estudiante.id == clave:
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
        return None"""
