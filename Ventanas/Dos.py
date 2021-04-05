from tkinter import *
from Funciones.FuncionesSimples import FuncionesS

class Dos:


    def window():
        raiz = Tk()
        miFrame = Frame(raiz,width=1000, height=500)
        miFrame.pack()
        raiz.title("Operaciones con dos imagenes")
        raiz.resizable(False,False)

        # ----------------------------- BARRA DE MENU -----------------------------------------
        barraMenu = Menu(raiz)
        raiz.config(menu=barraMenu)
        AbrirArchivo = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="AbrirArchivo", menu=AbrirArchivo)
        Operaciones = Menu(barraMenu, tearoff=0)
        barraMenu.add_cascade(label="Operaciones", menu=Operaciones)
        Operaciones.add_command(label="Unión")
        Operaciones.add_command(label="Intersección")
        Operaciones.add_command(label="Diferencia")
        Operaciones.add_command(label="Diferencia simétrica")
        Reportes = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Reportes", menu=Reportes)
        Reportes.add_command(label="Generar Reporte")
        Ayuda = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Ayuda", menu=Ayuda)
        Ayuda.add_command(label="Informacion",command= lambda: FuncionesS.informacion())
        Ayuda.add_command(label="Documentacion",command= lambda: FuncionesS.docu())

        #--------- Botones -----------
        boton1 = Button(raiz,text="Mostrar 1")
        boton2 = Button(raiz,text="Mostrar 2")
        boton3 = Button(raiz,text="Resultado")
        

        raiz.mainloop()

Dos.window()