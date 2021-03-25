from tkinter import messagebox
from tkinter import filedialog
import xml.etree.ElementTree as ET

class FuncionesS:

    def informacion():
        messagebox.showinfo("IPC2","Proyecto 2\nCreado por: Bryan Eduardo Caal Racanac\nCarnet: 201801155")

    def abrirArchivo():
        file_path = filedialog.askopenfilename(initialdir = "", title = "Abrir Archivo", filetypes = (("text files", "*.xml"),("all files", "*.*")) )
        
        return file_path

    def datosXML():
        path = FuncionesS.abrirArchivo()
        tree = ET.parse(path)
        root = tree.getroot()

        for elem in root:
            #nombre = elem[0].text
            #fila = elem[1].text
            #columna = elem[2].text
            imagen = elem[3].text
            imagen = list(imagen)
            print(imagen)

FuncionesS.datosXML()