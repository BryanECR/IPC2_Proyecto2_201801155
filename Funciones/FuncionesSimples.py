from tkinter import messagebox
from tkinter import filedialog
import xml.etree.ElementTree as ET

class FuncionesS:

    def AnalizadorImagen(cadena):
        cadena = str(cadena).replace('\t',"").replace(" ","")
        cadena = cadena.split('\n')
        
        new = []
        for i in range(len(cadena)):
            var = list(cadena[i])
            if len(var) > 1:
                new.append(var)

        for f in range(len(new)):
            for c in range(len(new[f])):
                if str(new[f][c]) == "*":
                    print('posicion['+str(f)+']['+str(c)+'] = '+str(new[f][c]) )
                



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
            imagen = elem[3].text
            FuncionesS.AnalizadorImagen(imagen)

FuncionesS.datosXML()