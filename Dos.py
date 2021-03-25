from tkinter import *

raiz = Tk()
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


Ayuda = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=Ayuda)
Ayuda.add_command(label="Informacion")
Ayuda.add_command(label="Documentacion")


miFrame = Frame(raiz,width=1000, height=500)
miFrame.pack()


raiz.mainloop()