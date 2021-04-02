from Listas.nodos import Nodo

class listaEncabezados:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregarEncabezado(self,id):
        
        if self.vacia():
            self.primero = self.ultimo =  Nodo(id)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(id)
            self.ultimo.anterior = aux

    def obtenerEncabezado(self,buscar):
        if self.vacia():
            print("No hay elementos el al cabecera")

        else:
            aux = self.primero
            while aux.siguiente != None:
                if aux.id == buscar:
                    return aux
                    
                aux = aux.siguiente
            
            if aux.id == buscar:
                return aux
            
    def recorrer(self):
        if self.vacia():
            print("No hay elementos")

        else:
            aux = self.primero
            while aux.siguiente != None:

                print(aux.id)

                aux = aux.siguiente
            
            print(aux.id)
