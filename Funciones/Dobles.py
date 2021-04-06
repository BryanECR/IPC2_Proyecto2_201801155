from Funciones.FuncionesSimples import FuncionesS
import xml.etree.ElementTree as ET
import time
import os
from Listas.matriz import Matriz
from tkinter import messagebox


matrix1 = Matriz()
matrix2 = Matriz()
table = []
matrices = []

class Dobles:

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
        os.system("dot -Tpng "+nombre+".dot -o "+nombre+".png")
        from Ventanas.Dos import Dos
        Dos.opActual(nombre)
        print("***")

    def matrixOriginal(matriz):
        matrix = matriz
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

        return matgrap

    def datosXML():
        path = FuncionesS.abrirArchivo()
        tree = ET.parse(path)
        root = tree.getroot()

        imagenes = []
        for elem in root:
            nombre = elem[0].text
            filas = int(elem[1].text)
            columnas = int(elem[2].text)
            imagen = elem[3].text
            info = {"Nombre":nombre,"Filas":filas,"Columnas":columnas,"Imagen":imagen}
            imagenes.append(info)
            
        

        #CREAR LOS ENCABEZADOS
        matrix1.crearEncabezados(imagenes[0]['Filas'],imagenes[0]['Columnas'])
        
        #ANALIZAR CADENAS
        cadena = str(imagenes[0]['Imagen']).replace('\t',"").replace(" ","")
        cadena = cadena.split('\n')
        ellenos = 0
        evacios = 0

        new = []
        #LLENAR LA MATRIZ CON LOS VALORES DE LA CADENA
        for i in range(len(cadena)):
                    var = list(cadena[i])
                    if len(var) > 1:
                        new.append(var)

        for f in range(len(new)):
            for c in range(len(new[f])):
                if str(new[f][c]) == "*":
                    matrix1.insertarCelda(f,c,"*")
                    ellenos += 1
                else:
                    matrix1.insertarCelda(f,c,"-")
                    evacios += 1

        tiempo = str(time.strftime("%X"))
        fecha = str(time.strftime("%x")) 
        infoM = {"Fecha":fecha,"Hora":tiempo,"Nombre":imagenes[0]['Nombre'],"Ellenos":ellenos,"Evacios":evacios }
        matrices.append(infoM)
        mat1 = Dobles.matrixOriginal(matrix1)
        Dobles.graficar("Matriz1",mat1)

        #---------------------------------------- PRIMERA ------------------------------------------------

        #CREAR LOS ENCABEZADOS
        matrix2.crearEncabezados(imagenes[0]['Filas'],imagenes[0]['Columnas'])

        #ANALIZAR CADENAS
        cadena = str(imagenes[1]['Imagen']).replace('\t',"").replace(" ","")
        cadena = cadena.split('\n')
        ellenos = 0
        evacios = 0

        new = []
        #LLENAR LA MATRIZ CON LOS VALORES DE LA CADENA
        for i in range(len(cadena)):
                    var = list(cadena[i])
                    if len(var) > 1:
                        new.append(var)

        for f in range(len(new)):
            for c in range(len(new[f])):
                if str(new[f][c]) == "*":
                    matrix2.insertarCelda(f,c,"*")
                    ellenos += 1
                else:
                    matrix2.insertarCelda(f,c,"-")
                    evacios += 1
        
        infoM = {"Fecha":fecha,"Hora":tiempo,"Nombre":imagenes[1]['Nombre'],"Ellenos":ellenos,"Evacios":evacios }
        matrices.append(infoM)
        mat2 = Dobles.matrixOriginal(matrix2)
        Dobles.graficar("Matriz2",mat2)

    #hacer de las 2 matrices una con los elementos de las 2
    def union(mat1,mat2):
        new = []
        for f in range(len(mat1)):
            new.append([])
            for c in range(len(mat1[0])):
                if str(mat1[f][c]) == str(mat2[f][c]):
                    new[f].append(mat1[f][c])
                elif str(mat1[f][c]) != str(mat2[f][c]):
                    if mat1[f][c] == "*" or mat2[f][c]== "*":
                        new[f].append("*")

        Dobles.graficar("Union",new)

    #Solo elementos repetidos entre las 2 matrices
    def interseccion(mat1,mat2):
        new = []
        for f in range(len(mat1)):
            new.append([])
            for c in range(len(mat1[0])):
                if str(mat1[f][c]) == str(mat2[f][c]):
                    new[f].append(mat1[f][c])
                else:
                    new[f].append(" ")
        
        Dobles.graficar("Interseccion",new)

    def simetrica(mat1,mat2):
        new = []
        for f in range(len(mat1)):
                new.append([])
                for c in range(len(mat1[0])):
                    if str(mat1[f][c]) == str(mat2[f][c]):
                        new[f].append(mat1[f][c])
                    else:
                        new[f].append(" ")
        
        Dobles.graficar("Simetria",new)

    #TODOS LOS DE A QUE NO PERTENEZCAN A B
    def diferencia(mat1,mat2):
        new = []
        for f in range(len(mat1)):
            new.append([])
            for c in range(len(mat1[0])):
                if str(mat1[f][c]) != " " and str(mat2[f][c]) == " ":  
                    new[f].append(mat1[f][c])
                else:  
                    new[f].append(" ")
              
        Dobles.graficar("Diferencia",new)


    def Operaciones(operacion):
        tiempo = str(time.strftime("%X"))
        fecha = str(time.strftime("%x")) 

        if str(operacion) == "Union":
            print(fecha+"   "+tiempo+"   Union")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
            mat1 = Dobles.matrixOriginal(matrix1)
            mat2 = Dobles.matrixOriginal(matrix2)
            Dobles.union(mat1,mat2)

        elif str(operacion) == "Interseccion":
            print(fecha+"   "+tiempo+"   Interseccion")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
            mat1 = Dobles.matrixOriginal(matrix1)
            mat2 = Dobles.matrixOriginal(matrix2)
            Dobles.interseccion(mat1,mat2)

        elif str(operacion) == "Simetrica":
            print(fecha+"   "+tiempo+"   Simetrica")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
            mat1 = Dobles.matrixOriginal(matrix1)
            mat2 = Dobles.matrixOriginal(matrix2)
            Dobles.simetrica(mat1,mat2)

        elif str(operacion) == "Diferencia":
            print(fecha+"   "+tiempo+"   Diferencia")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
            mat1 = Dobles.matrixOriginal(matrix1)
            mat2 = Dobles.matrixOriginal(matrix2)
            Dobles.diferencia(mat1,mat2)

    def reporte():
        global info
        html = '''
        <!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="UTF-8">
        <title>Reporte Operaciones con dos Matrices</title>
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
        for i in range(len(matrices)):
            html += '\n<tr>\n<th scope="row">'+str(matrices[i]['Fecha'])+'</th>\n<th>'+str(matrices[i]['Hora'])+'</th>\n<th>'+str(matrices[i]['Nombre'])+'</th>\n<th>'+str(matrices[i]['Ellenos'])+'</th>\n<th>'+str(matrices[i]['Evacios'])+'</th>\n</tr>\n'

        html+= ''' </tbody>
        </table>
        <h1 class="titulo" align="center" >Reporte</h1>
        <table class="table table-dark table-striped" align="center">
        <thead>
        <tr>
        <th scope="col">Fecha</th>
        <th scope="col">Hora</th>
        <th scope="col">Tipo de Operacion</th>
        </tr>
        </thead>\n<tbody>'''

        for i in range(len(table)):
            html += '\n<tr>\n<th scope="row">'+str(table[i]['Fecha'])+'</th>\n<th>'+str(table[i]['Hora'])+'</th>\n<th>'+str(table[i]['Operacion'])+'</th>\n</tr>\n'
        

        html += '''\n</tbody>\n</table>\n</div>\n</body>\n</html> '''

        file = open("Reporte2.html","w")
        file.write(html)
        file.close()

        messagebox.showinfo("Reporte","Reporte Generado con exito")
        
