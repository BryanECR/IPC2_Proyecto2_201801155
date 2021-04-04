from tkinter import messagebox
from tkinter import filedialog
import xml.etree.ElementTree as ET
import time
from Listas.matriz import Matriz
import os

table = []
info = {}
matrix = Matriz()
class FuncionesS:

    def graficar(nombre,mat):
        cadena = "<TR>\n<TD>A</TD>\n"
        contador = 0
        while( contador < len(mat[0])):
            cadena += "<TD>"+str(contador)+"</TD>\n"
            contador += 1 
        cadena+="</TR>\n"

        fila = 0
        while( fila < len(mat) ):
            cadena += "<TR>\n<TD>"+str(fila)+"</TD>\n"
            columna = 0
            while(columna < len(mat[0])):
                cadena += "<TD>"+str(mat[fila][columna])+"</TD>\n"
                columna += 1
            cadena += "</TR>\n"
            fila += 1
        
        file = open(nombre+".dot","w")
        file.write("digraph G {\n a[label=<\n<TABLE>\n"+cadena+'</TABLE>\n> shape="box"]\n}')
        file.close()
        os.system('dot -Tpng '+nombre+'.dot -o '+nombre+'.png')

        print("***")

    def matrizOriginal():
        Filas = matrix.Filas()
        Columnas = matrix.Columnas()

        matrixOriginal = []
        for i in range(Filas):
            matrixOriginal.append([0]*Columnas)

        datos = matrix.recorrerFilas()

        for i in range(len(datos)):
            f = datos[i]['Fila']
            c = datos[i]['Columna']
            cont = datos[i]['Contenido']
            if cont == "*":
                matrixOriginal[f][c] = "*"
            else:
                matrixOriginal[f][c] = " "

        return matrixOriginal

    def operaciones(Operacion):
        operacion = str(Operacion)
        tiempo = str(time.strftime("%X"))
        fecha = str(time.strftime("%x"))

        if operacion == "Rotación horizontal":
            print(fecha+"   "+tiempo+"   Rotación horizontal")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
        elif operacion == "Rotación vertical":
            print(fecha+"   "+tiempo+"   Rotación vertical")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
        elif operacion == "Transpuesta":
            print(fecha+"   "+tiempo+"   Transpuesta")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
        #--------------------- OPERACIONES CON PARAMETROS --------------------------
        elif operacion == "Limpiar zona":
            print(fecha+"   "+tiempo+"   Limpiar zona")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
            from Funciones.Ventanas import ventanas
            mat = FuncionesS.matrizOriginal() 
            ventanas.cuatro(mat)
        elif operacion == "Agregar línea horizontal":
            print(fecha+"   "+tiempo+"   Agregar línea horizontal")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
            from Funciones.Ventanas import ventanas
            mat = FuncionesS.matrizOriginal() 
            ventanas.cinco(mat)
            
        elif operacion == "Agregar línea vertical":
            print(fecha+"   "+tiempo+"   Agregar línea vertical")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
            from Funciones.Ventanas import ventanas
            mat = FuncionesS.matrizOriginal() 
            ventanas.seis(mat)
            
        elif operacion == "Agregar rectángulo":
            print(fecha+"   "+tiempo+"   Agregar rectángulo")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
            from Funciones.Ventanas import ventanas
            mat = FuncionesS.matrizOriginal() 
            ventanas.siete(mat)
        elif operacion == "Agregar triángulo rectángulo":
            print(fecha+"   "+tiempo+"   Agregar triángulo rectángulo")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
            from Funciones.Ventanas import ventanas
            mat = FuncionesS.matrizOriginal() 
            ventanas.ocho(mat)
            
    def AnalizadorImagen(nombre,cadena,filas,columnas):
        global info, matrix
        matrix.crearEncabezados(filas,columnas)
        cadena = str(cadena).replace('\t',"").replace(" ","")
        cadena = cadena.split('\n')
        ellenos = 0
        evacios = 0
        
        new = []
        for i in range(len(cadena)):
            var = list(cadena[i])
            if len(var) > 1:
                new.append(var)

        for f in range(len(new)):
            for c in range(len(new[f])):
                if str(new[f][c]) == "*":
                    matrix.insertarCelda(int(f),int(c),new[f][c])
                    ellenos += 1
                else:
                    matrix.insertarCelda(int(f),int(c),new[f][c])
                    evacios += 1
        
        info = {"Fecha":str(time.strftime("%x")),"Hora":str(time.strftime("%X")),"Nombre":nombre,"Ellenos":ellenos,"Evacios":evacios}

        #OBTENER FILAS Y COLUMNAS PARA LA GRAFICA
        Filas = matrix.Filas()
        Columnas = matrix.Columnas()

        matgrap = []
        for i in range(Filas):
            matgrap.append([0]*Columnas)

        datos = matrix.recorrerFilas()

        for i in range(len(datos)):
            f = datos[i]['Fila']
            c = datos[i]['Columna']
            cont = datos[i]['Contenido']
            if cont == "*":
                matgrap[f][c] = "*"
            else:
                matgrap[f][c] = " "

        FuncionesS.graficar("normal",matgrap)
                
    def informacion():
        messagebox.showinfo("IPC2","Proyecto 2\nCreado por: Bryan Eduardo Caal Racanac\nCarnet: 201801155")

    def docu():
        os.system("Documentacion-P2.pdf")

    def abrirArchivo():
        file_path = filedialog.askopenfilename(initialdir = "", title = "Abrir Archivo", filetypes = (("text files", "*.xml"),("all files", "*.*")) )
        
        return file_path

    def datosXML():
        path = FuncionesS.abrirArchivo()
        tree = ET.parse(path)
        root = tree.getroot()

        for elem in root:
            nombre = elem[0].text
            filas = int(elem[1].text)
            columnas = int(elem[2].text)
            imagen = elem[3].text
            FuncionesS.AnalizadorImagen(nombre,imagen,filas,columnas)

    def reporte():
        global info
        html = ''' <!DOCTYPE html>
            <html lang="es">
            <head>
            <meta charset="UTF-8">
            <title>Reporte Operaciones Simples</title>
            <!-- CSS only -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
            <style>
            *{
            margin: 0px;
            padding: 0px;
            }
            body{
            background-color: beige;
            }
            .titulo{
            font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            }
            .content{
            align-content: center;
            margin: 30px;
            padding: 5%;
            }
            </style>
            </head>
            <body>
            <div class="content">
            <h1 class="titulo" align="center">Datos de matriz</h1>
            <table class="table table-dark table-striped" align="center">
            <thead>
            <tr>
            <th scope="col">Fecha</th>
            <th scope="col">Hora</th>
            <th scope="col">Nombre</th>
            <th scope="col">No. Espacios llenos</th>
            <th scope="col">No. Espacios vacios</th>
            </tr>
            </thead>
            <tbody>
            '''

        
        html += '\n<tr>\n<th scope="row">'+str(info['Fecha'])+'</th>\n<th>'+str(info['Hora'])+'</th>\n<th>'+str(info['Nombre'])+'</th>\n<th>'+str(info['Ellenos'])+'</th>\n<th>'+str(info['Evacios'])+'</th>\n</tr>\n'

        html+= ''' </tbody>
            </table>
            <h1 class="titulo" align="center" >Reporte</h1>
            <table class="table table-dark table-striped" align="center">
            <thead>
            <tr>
            <th scope="col">Fecha</th>
            <th scope="col">Hora</th>
            <th scope="col">Tipo de Operacion</th>
            <th scope="col">Nombre</th>
            </tr>
            </thead>\n<tbody>'''

        for i in range(len(table)):
            html += '\n<tr>\n<th scope="row">'+str(table[i]['Fecha'])+'</th>\n<th>'+str(table[i]['Hora'])+'</th>\n<th>'+str(table[i]['Operacion'])+'</th>\n<th>'+str(info['Nombre'])+'</th> \n</tr>\n'
        

        html += '''\n</tbody>\n</table>\n</div>\n</body>\n</html> '''

        file = open("Reporte1.html","w")
        file.write(html)
        file.close()

        messagebox.showinfo("Reporte","Reporte Generado con exito")

    
