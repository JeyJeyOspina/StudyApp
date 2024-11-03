class ErrorBase(Exception):
    pass


class EntradaInvalidaError(ErrorBase):
    def __init__(self, mensaje="Entrada no válida. Por favor, revise el formato e intente de nuevo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class UsuarioNoEncontradoError(ErrorBase):
    def __init__(self, usuario):
        self.usuario = usuario
        self.mensaje = f"Usuario '{self.usuario}' no encontrado."
        super().__init__(self.mensaje)


class GrupoNoEncontradoError(ErrorBase):
    def __init__(self, grupo):
        self.grupo = grupo
        self.mensaje = f"Grupo de estudio '{self.grupo}' no encontrado."
        super().__init__(self.mensaje)


class EventoFechaPasadaError(ErrorBase):
    def __init__(self, mensaje="No se pueden agregar eventos en una fecha pasada."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
