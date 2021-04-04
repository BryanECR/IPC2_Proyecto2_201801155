from tkinter import *
from Funciones.FuncionesSimples import FuncionesS
from PIL import ImageTk,Image

class Simples:

    def __init__(self):
        pass

    def ventanaSimple():
        raiz = Tk()
        miFrame = Frame(raiz,width=800, height=500)
        miFrame.pack()
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
        Operaciones.add_command(label="Rotación horizontal", command= lambda: FuncionesS.operaciones("Rotación horizontal"))
        Operaciones.add_command(label="Rotación vertical", command= lambda: FuncionesS.operaciones("Rotación vertical") ) 
        Operaciones.add_command(label="Transpuesta", command= lambda: FuncionesS.operaciones("Transpuesta") )
        Operaciones.add_command(label="Limpiar zona", command= lambda: FuncionesS.operaciones("Limpiar zona") ) 
        Operaciones.add_command(label="Agregar línea horizontal", command= lambda: FuncionesS.operaciones("Agregar línea horizontal")) 
        Operaciones.add_command(label="Agregar línea vertical", command= lambda: FuncionesS.operaciones("Agregar línea vertical") ) 
        Operaciones.add_command(label="Agregar rectángulo", command= lambda: FuncionesS.operaciones("Agregar rectángulo") ) 
        Operaciones.add_command(label="Agregar triángulo rectángulo", command= lambda: FuncionesS.operaciones("Agregar triángulo rectángulo") ) 

        Reportes = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Reportes", menu=Reportes)
        Reportes.add_cascade(label="Generar Reporte", command= lambda:FuncionesS.reporte() )

        Ayuda = Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Ayuda", menu=Ayuda)
        Ayuda.add_command(label="Informacion",command= lambda: FuncionesS.informacion() )
        Ayuda.add_command(label="Documentacion",command= lambda: FuncionesS.docu() )

        

        #----------------------------------------- COLOCAR LABELS PARA MOSTRAR IMAGENES ---------------------------------------
        label1 = Label(miFrame,text="Matriz Oroginal",font=18)
        label1.place(x=100,y=20)
        label2 = Label(miFrame,text="Resultado",font=18)
        label2.place(x=600,y=20)

        def Original():
            try:
                imagen = ImageTk.PhotoImage(Image.open(r"normal.png"))
                labelimagen = Label(image=imagen).place(x=10,y=50)
            except:
                print("No se encontro la Imagen")


        boton = Button(miFrame,text="Mostrar Original",font=15)
        boton.place(x=100,y=450)

        boton2 = Button(miFrame,text="Mostrar Resultado",font=15)
        boton2.place(x=500,y=450)
        boton3 = Button(miFrame,text="Borrar",font=15)
        boton3.place(x=700,y=450)


        
        raiz.mainloop()

