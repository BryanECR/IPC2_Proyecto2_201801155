from tkinter import messagebox
from tkinter import filedialog
import xml.etree.ElementTree as ET
import time

table = []
info = {}
class FuncionesS:

    def tres(uno,dos,tres):
        print(uno,dos,tres)

    #FALTAN AGREGAR LAS FUNCIONES PARA REALIZAR LAS OPERACIONES Y RECIBIR COMO PARAMETRO EL NOMBRE DE LA MATRIX
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
        elif operacion == "Limpiar zona":
            print(fecha+"   "+tiempo+"   Limpiar zona")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
        elif operacion == "Agregar línea horizontal":
            print(fecha+"   "+tiempo+"   Agregar línea horizontal")
            #--------------------------------------
            from Funciones.Ventanas import ventanas
            ventanas.cinco()
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
        elif operacion == "Agregar línea vertical":
            print(fecha+"   "+tiempo+"   Agregar línea vertical")
            #--------------------------------------
            from Funciones.Ventanas import ventanas
            ventanas.seis()
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
        elif operacion == "Agregar rectángulo":
            print(fecha+"   "+tiempo+"   Agregar rectángulo")
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)
        elif operacion == "Agregar triángulo rectángulo":
            print(fecha+"   "+tiempo+"   Agregar triángulo rectángulo")
            #--------------------------------------
            from Funciones.Ventanas import ventanas
            ventanas.ocho()
            operaciones = {"Fecha":fecha,"Hora":tiempo,"Operacion": operacion}
            table.append(operaciones)

    #FALTA AGREGAR LOS VALORES A LA LISTA ORTOGONAL PARA PODERLA MANEJAR
    def AnalizadorImagen(nombre,cadena):
        global info
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
                    print('posicion['+str(f)+']['+str(c)+'] = '+str(new[f][c]) )
                    ellenos += 1
                else:
                    evacios += 1
        
        info = {"Fecha":str(time.strftime("%x")),"Hora":str(time.strftime("%X")),"Nombre":nombre,"Ellenos":ellenos,"Evacios":evacios}
                
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
            nombre = elem[0].text
            imagen = elem[3].text
            FuncionesS.AnalizadorImagen(nombre,imagen)

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

    
