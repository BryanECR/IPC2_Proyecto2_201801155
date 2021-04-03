from tkinter import *
from Simples import Simples

class Opciones:

    def ventanaOpciones():
        root = Tk()
        root.title("Opciones")
        root.resizable(False,False)
        miFrame = Frame(root, width=300,height=150)
        miFrame.pack()

        Label(miFrame,text="Tipo de Operacion que desea realizar",font=(10)).place(x= 15,y=20)

        def simples():
            root.destroy()
            Simples.ventanaSimple()
            

        botonSimple = Button(root,text="Simples", command= simples ).place(x=120,y=60)

        botonDoble = Button(root, text="Con dos imagenes" ).place(x=90,y=100)

        root.mainloop()

if __name__ == "__main__":
    Opciones.ventanaOpciones()