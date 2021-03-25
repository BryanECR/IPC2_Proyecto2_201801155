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

        AbrirArchivo = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="AbrirArchivo", menu=AbrirArchivo)

        Operaciones = Menu(barraMenu, tearoff=0)
        barraMenu.add_cascade(label="Operaciones", menu=Operaciones)
        Operaciones.add_command(label="Rotación horizontal")
        Operaciones.add_command(label="Rotación vertical")
        Operaciones.add_command(label="Transpuesta")
        Operaciones.add_command(label="Limpiar zona")
        Operaciones.add_command(label="Agregar línea horizontal")
        Operaciones.add_command(label="Agregar línea vertical")
        Operaciones.add_command(label="Agregar rectángulo")
        Operaciones.add_command(label="Agregar triángulo rectángulo")

        Reportes = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Reportes", menu=Reportes)

        Ayuda = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Ayuda", menu=Ayuda)
        Ayuda.add_command(label="Informacion",command= FuncionesS.informacion )
        Ayuda.add_command(label="Documentacion")


        miFrame = Frame(raiz,width=600, height=500)
        miFrame.pack()


        raiz.mainloop()

