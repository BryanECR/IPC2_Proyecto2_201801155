from tkinter import *
from Funciones.FuncionesSimples import FuncionesS


class Simples:

    def __init__(self):
        pass

    def ventanaSimple():
        raiz = Tk()
        raiz.title("Operaciones Simples")
        raiz.resizable(False,False)

        # ----------------------------- BARRA DE MENU -----------------------------------------
        barraMenu = Menu(raiz)
        raiz.config(menu=barraMenu)

        Abrir = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Abrir", menu=Abrir)
        Abrir.add_cascade(label="Abrir Archivo", command= lambda: FuncionesS.datosXML() )

        Operaciones = Menu(barraMenu, tearoff=0)
        barraMenu.add_cascade(label="Operaciones", menu=Operaciones)
        Operaciones.add_command(label="Rotación horizontal", command= lambda: FuncionesS.timeDate("Rotación horizontal"))
        Operaciones.add_command(label="Rotación vertical", command= lambda: FuncionesS.timeDate("Rotación vertical") ) 
        Operaciones.add_command(label="Transpuesta", command= lambda: FuncionesS.timeDate("Transpuesta") )
        Operaciones.add_command(label="Limpiar zona", command= lambda: FuncionesS.timeDate("Limpiar zona") ) 
        Operaciones.add_command(label="Agregar línea horizontal", command= lambda: FuncionesS.timeDate("Agregar línea horizontal")) 
        Operaciones.add_command(label="Agregar línea vertical", command= lambda: FuncionesS.timeDate("Agregar línea vertical") ) 
        Operaciones.add_command(label="Agregar rectángulo", command= lambda: FuncionesS.timeDate("Agregar rectángulo") ) 
        Operaciones.add_command(label="Agregar triángulo rectángulo", command= lambda: FuncionesS.timeDate("Agregar triángulo rectángulo") ) 

        Reportes = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Reportes", menu=Reportes)
        Reportes.add_cascade(label="Generar Reporte", command= lambda:FuncionesS.reporte() )

        Ayuda = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Ayuda", menu=Ayuda)
        Ayuda.add_command(label="Informacion",command= lambda: FuncionesS.informacion() )
        
        Ayuda.add_command(label="Documentacion")


        miFrame = Frame(raiz,width=800, height=500)
        miFrame.pack()


        raiz.mainloop()

