from tkinter import *
from Simples import Simples

class Opciones:

    def ventanaOpciones():
        raiz = Tk()
        raiz.title("Opciones")
        raiz.resizable(False,False)
        miFrame = Frame(raiz, width=300,height=150)
        miFrame.pack()

        Label(miFrame,text="Tipo de Operacion que desea realizar",font=(10)).place(x= 15,y=20)

        botonSimple = Button(raiz,text="Simples", command= lambda: Simples.ventanaSimple() ).place(x=120,y=60)

        botonDoble = Button(raiz, text="Con dos imagenes" ).place(x=90,y=100)

        raiz.mainloop()

if __name__ == "__main__":
    Opciones.ventanaOpciones()