from tkinter import *
from Funciones.FuncionesSimples import FuncionesS

class ventanas:
    def cuatro(mat):
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

        def limpiarZona(fInicio,cInicio,fFinal,cFinal,mat):
            while(fInicio <= fFinal):
                contador = cInicio
                while(contador <= cFinal):
                    mat[fInicio][contador] = " "
                    contador += 1
                fInicio += 1
    
            FuncionesS.graficar("Limpiar",mat)
        
        def click():
            F1 = int(Fb.get())-1
            C1 = int(Cb.get())-1
            F2 = int(Fe.get())-1
            C2 = int(Ce.get())-1
            matrix = mat
            root.destroy()
            limpiarZona(F1,C1,F2,C2,matrix)

        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        
        root.mainloop()

    def cinco(mat):
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

        def lHorizontal(fila,columna,Nelementos,mat):
            contador = columna
            elem = columna+Nelementos
            while(contador < elem):
                #print("Fila "+str(fila)+" Columna "+str(contador))
                mat[fila][contador] = "0"
                contador += 1

            FuncionesS.graficar("LHorizontal",mat)

        def click():
            P1 = int(parametro1.get())
            P2 = int(parametro2.get())
            P3 = int(parametro3.get())
            FuncionesS.tres(P1,P2,P3)
            matrix = mat
            root.destroy()
            lHorizontal(P1,P2,P3,matrix)

        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        root.mainloop()

    def seis(mat):
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

        def lVertical(fila,columna,Nelementos,mat):
            contador = fila
            elem = fila+Nelementos
            while(contador < elem):
                mat[contador][columna] = "0"
                contador += 1

            FuncionesS.graficar("LVertical",mat)
        
        def click():
            P1 = int(parametro1.get())
            P2 = int(parametro2.get())
            P3 = int(parametro3.get())
            matrix = mat
            root.destroy()
            lVertical(P1,P2,P3,matrix)

        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        
        root.mainloop()

    def siete(mat):
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
        
        def rectangulo(fila,columna,alto,ancho,mat):
            fFinal = columna+alto
            cFinal = fila+ancho
            while(fila < fFinal):
                contador = columna
                while(contador < cFinal):
                    #print("Fila "+str(fila)+" Columna "+str(contador))
                    mat[fila][contador] = "0"
                    contador += 1
                fila += 1
            
            FuncionesS.graficar("AddRectangulo",mat)
        
        def click():
            P1 = int(parametro1.get())
            P2 = int(parametro2.get())
            P3 = int(parametro2.get())
            P4 = int(parametro4.get())
            matrix = mat
            root.destroy()
            rectangulo(P1,P2,P3,P4,matrix)

        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        
        root.mainloop()

    def ocho(mat):
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

        def trianguloRectangulo(fila,columna,lon,mat):
            fFinal = fila+lon
            avanzar = columna+1
            while(fila < fFinal):
                #print("Fila "+str(fila))
                contador = columna
                while(contador < avanzar):
                    #print("Fila "+str(fila)+ " Columna "+str(contador))
                    mat[fila][contador] = "0"
                    contador += 1

                avanzar +=1
                fila +=1

            FuncionesS.graficar("Triangulo",mat)
        
        def click():
            P1 = int(parametro1.get())
            P2 = int(parametro2.get())
            P3 = int(parametro3.get())
            matrix = mat
            root.destroy()
            trianguloRectangulo(P1,P2,P3,matrix)


        boton = Button( root,text="Aceptar",command=click )
        boton.grid(row=4,column=1,sticky=W)
        
        root.mainloop()

