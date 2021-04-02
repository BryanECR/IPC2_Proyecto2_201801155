from Listas.nodos import Celda
from Listas.encabezado import listaEncabezados

class Matriz:
    def __init__(self):
        self.eFilas = listaEncabezados()
        self.eColumnas = listaEncabezados()

    def crearEncabezados(self,filas,columnas):
        for i in range(filas):
            self.eFilas.agregarEncabezado(i)
        
        for i in range(columnas):
            self.eColumnas.agregarEncabezado(i)
            
    def insertarCelda(self,fila,columna,contenido):
        nuevo = Celda(fila,columna,contenido)

        #HACER CONEXIONES POR FILAS
        eFila = self.eFilas.obtenerEncabezado(fila)
        if nuevo.fila == eFila.id:
            nuevo.derecha = eFila.acceso
            nuevo.izquierda = eFila.acceso
            eFila.acceso = nuevo

        #HACER CONEXIONES POR COLUMNAS
        eColumna = self.eColumnas.obtenerEncabezado(columna)
        if nuevo.columna == eColumna.id:
            nuevo.abajo = eColumna.acceso
            nuevo.arriba = eColumna.acceso
            eColumna.acceso = nuevo  


    def recorrerFilas(self):
        eFila = self.eFilas.primero
        datos = []
        while eFila != None:

            actual = eFila.acceso
            try:
                Fila = actual.fila
            except:
                break
            
            while actual != None:

                informacion = {"Fila":Fila,"Columna":actual.columna,"Contenido":actual.contenido}
                datos.append(informacion)   

                actual = actual.izquierda
            try:
                eFila = eFila.siguiente
            except:
                continue

        return datos
 
    def Filas(self):
        eFila = self.eFilas.primero
        contador = 0
        while eFila != None:
            contador += 1
            eFila = eFila.siguiente

        return contador

    def Columnas(self):
        eColumna = self.eColumnas.primero
        contador = 0
        while eColumna != None:
            contador += 1
            eColumna = eColumna.siguiente

        return contador 

    



