from tkinter import *
from Funciones.FuncionesSimples import FuncionesS

class ventanas:
    def cuatro():
        root = Tk()
        root.title('Limpieza de area')
        root.geometry('400x200')

        Fb = Entry(root)
        Fb.grid(row=0,column=1)
        Cb = Entry(root)
        Cb.grid(row=1,column=1)
        Fe = Entry(root)
        Fe.grid(row=2,column=1)
        Ce = Entry(root)
        Ce.grid(row=3,column=1)
        

        l1 = Label(root,text='Fila donde comienza',font=(14))
        l1.grid(row=0,column=0,padx=5,pady=5)
        l2 = Label(root,text='Columna donde comienza',font=(14))
        l2.grid(row=1,column=0,padx=5,pady=5)
        l3 = Label(root,text='Fila donde termina',font=(14))
        l3.grid(row=2,column=0,padx=5,pady=5)
        l4 = Label(root,text='Columna donde termina',font=(14))
        l4.grid(row=3,column=0,padx=5,pady=5)
        
        def click():
            F1 = int(Fb.get())
            C1 = int(Cb.get())
            F2 = int(Fe.get())
            C2 = int(Ce.get())
            #AGREGAR LA FUNCION A DONDE SE VAN A MANDAR LOS PARAMETROS
            root.destroy()


        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        
        root.mainloop()

    def cinco():
        root = Tk()
        root.title('Agregar linea horizontal')
        root.geometry('400x200')

        parametro1 = Entry(root)
        parametro1.grid(row=0,column=1)
        parametro2 = Entry(root)
        parametro2.grid(row=1,column=1)
        parametro3 = Entry(root)
        parametro3.grid(row=2,column=1)  

        l1 = Label(root,text='Fila donde comienza',font=(14))
        l1.grid(row=0,column=0,padx=5,pady=5)
        l2 = Label(root,text='Columna donde comienza',font=(14))
        l2.grid(row=1,column=0,padx=5,pady=5)
        l3 = Label(root,text='Cantidad de elementos',font=(14))
        l3.grid(row=2,column=0,padx=5,pady=5)
        
        def click():
            P1 = int(parametro1.get())
            P2 = int(parametro2.get())
            P3 = int(parametro3.get())
            FuncionesS.tres(P1,P2,P3)
            #AGREGAR LA FUNCION A DONDE SE VAN A MANDAR LOS PARAMETROS
            root.destroy()

        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        
        root.mainloop()

    def seis():
        root = Tk()
        root.title('Agregar linea vertical')
        root.geometry('400x150')

        parametro1 = Entry(root)
        parametro1.grid(row=0,column=1)
        parametro2 = Entry(root)
        parametro2.grid(row=1,column=1)
        parametro3 = Entry(root)
        parametro3.grid(row=2,column=1)

        l1 = Label(root,text='Fila donde comienza',font=(14))
        l1.grid(row=0,column=0,padx=5,pady=5)
        l2 = Label(root,text='Columna donde comienza',font=(14))
        l2.grid(row=1,column=0,padx=5,pady=5)
        l3 = Label(root,text='Cantidad de elementos',font=(14))
        l3.grid(row=2,column=0,padx=5,pady=5)
        
        def click():
            P1 = int(parametro1.get())
            P2 = int(parametro2.get())
            P3 = int(parametro3.get())
            FuncionesS.tres(P1,P2,P3)
            #AGREGAR LA FUNCION A DONDE SE VAN A MANDAR LOS PARAMETROS
            root.destroy()

        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        
        root.mainloop()

    def siete():
        root = Tk()
        root.title('Agregar rectangulo')
        root.geometry('400x150')

        parametro1 = Entry(root)
        parametro1.grid(row=0,column=1)
        parametro2 = Entry(root)
        parametro2.grid(row=1,column=1)
        parametro3 = Entry(root)
        parametro3.grid(row=2,column=1)
        parametro4 = Entry(root)
        parametro4.grid(row=3,column=1)
        
        l1 = Label(root,text='Fila donde comienza',font=(14))
        l1.grid(row=0,column=0,padx=5,pady=5)
        l2 = Label(root,text='Columna donde comienza',font=(14))
        l2.grid(row=1,column=0,padx=5,pady=5)
        l3 = Label(root,text='Filas de alto',font=(14))
        l3.grid(row=2,column=0,padx=5,pady=5)
        l4 = Label(root,text='Columnas de ancho',font=(14))
        l4.grid(row=3,column=0,padx=5,pady=5)
        
        def click():
            P1 = int(parametro1.get())
            P2 = int(parametro2.get())
            P3 = int(parametro2.get())
            P4 = int(parametro4.get())
            #AGREGAR LA FUNCION A DONDE SE VAN A MANDAR LOS PARAMETROS
            root.destroy()

        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        
        root.mainloop()

    def ocho():
        root = Tk()
        root.title('Agregar triangulo rectangulo')
        root.geometry('400x150')

        parametro1 = Entry(root)
        parametro1.grid(row=0,column=1)
        parametro2 = Entry(root)
        parametro2.grid(row=1,column=1)
        parametro3 = Entry(root)
        parametro3.grid(row=2,column=1)  

        l1 = Label(root,text='Fila donde comienza',font=(14))
        l1.grid(row=0,column=0,padx=5,pady=5)
        l2 = Label(root,text='Columna donde comienza',font=(14))
        l2.grid(row=1,column=0,padx=5,pady=5)
        l3 = Label(root,text='Tamaño de los catetos',font=(14))
        l3.grid(row=2,column=0,padx=5,pady=5)
        
        def click():
            P1 = int(parametro1.get())
            P2 = int(parametro2.get())
            P3 = int(parametro3.get())
            FuncionesS.tres(P1,P2,P3)
            #AGREGAR LA FUNCION A DONDE SE VAN A MANDAR LOS PARAMETROS
            root.destroy()

        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        
        root.mainloop()

