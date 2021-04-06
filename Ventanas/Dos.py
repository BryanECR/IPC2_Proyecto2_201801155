from tkinter import *
from Funciones.Dobles import Dobles
from Funciones.FuncionesSimples import FuncionesS
from PIL import ImageTk,Image

arr = []
class Dos:

    def opActual(nombre):
        arr.append(nombre)

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
        barraMenu.add_cascade(label="Abrir", menu=AbrirArchivo)
        AbrirArchivo.add_cascade(label="Abrir Archivo",command=lambda:Dobles.datosXML() )
        Operaciones = Menu(barraMenu, tearoff=0)
        barraMenu.add_cascade(label="Operaciones", menu=Operaciones)
        Operaciones.add_command(label="Unión",command=lambda:Dobles.Operaciones("Union") )
        Operaciones.add_command(label="Intersección",command=lambda:Dobles.Operaciones("Interseccion") )
        Operaciones.add_command(label="Diferencia",command=lambda:Dobles.Operaciones("Diferencia") )
        Operaciones.add_command(label="Diferencia simétrica",command=lambda:Dobles.Operaciones("Simetrica") )
        Reportes = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Reportes", menu=Reportes)
        Reportes.add_command(label="Generar Reporte")
        Ayuda = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Ayuda", menu=Ayuda)
        Ayuda.add_command(label="Informacion",command=lambda:FuncionesS.informacion() )
        Ayuda.add_command(label="Documentacion",command=lambda:FuncionesS.docu() )

        label1 = Label(raiz,text="Matriz 1",font=18).place(x=70,y=20)
        label2 = Label(raiz,text="Matriz 2",font=18).place(x=400,y=20)
        label3 = Label(raiz,text="Resultado",font=18).place(x=700,y=20)

        def mostrar1():
            try:
                imagen = ImageTk.PhotoImage(Image.open(r'Matriz1.png'))
                labelimagen = Label(raiz,image=imagen).place(x=30,y=50)
                raiz.mainloop()
            except:
                print("La imagen no existe")

        def mostrar2():
            try:
                imagen = ImageTk.PhotoImage(Image.open(r'Matriz2.png'))
                labelimagen = Label(raiz,image=imagen).place(x=300,y=50)
                raiz.mainloop()
            except:
                print("La imagen no existe")

        def mostrarOperaciones():
            if str(arr[-1]) == "Union":
                imagen = ImageTk.PhotoImage(Image.open(r'Union.png'))
                labelimagen = Label(raiz,image=imagen).place(x=70,y=50)
                raiz.mainloop()

            elif str(arr[-1]) == "Interseccion":
                imagen = ImageTk.PhotoImage(Image.open(r'Interseccion.png'))
                labelimagen = Label(raiz,image=imagen).place(x=700,y=50)
                raiz.mainloop()

            elif str(arr[-1]) == "Diferencia":
                imagen = ImageTk.PhotoImage(Image.open(r'Diferencia.png'))
                labelimagen = Label(raiz,image=imagen).place(x=700,y=50)
                raiz.mainloop()

            elif str(arr[-1]) == "Simetria":
                imagen = ImageTk.PhotoImage(Image.open(r'Simetria.png'))
                labelimagen = Label(raiz,image=imagen).place(x=700,y=50)
                raiz.mainloop()


        #--------- Botones -----------
        boton1 = Button(raiz,text="Mostrar 1",command=lambda:mostrar1() ).place(x=100,y=450)
        boton2 = Button(raiz,text="Mostrar 2",command=lambda:mostrar2() ).place(x=400,y=450)
        boton3 = Button(raiz,text="Mostrar Resultado",command=lambda:mostrarOperaciones() ).place(x=700,y=450)
        

        raiz.mainloop()
