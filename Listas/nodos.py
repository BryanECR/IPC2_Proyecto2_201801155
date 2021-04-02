class Celda:
    def __init__(self, fila, columna, contenido):
        self.contenido = contenido
        self.fila = fila
        self.columna = columna
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None

class Nodo:
    def __init__(self,id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None