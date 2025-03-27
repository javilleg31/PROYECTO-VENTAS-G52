import libreria
import os
from tabulate import tabulate
from colorama import Fore, Back, Style, init
init()

from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generarPDF (encabezado, clientes):
    # Combinar encabezado con datos
    contenido = [encabezado] + clientes

    # Configurar el documento PDF
    nombre_pdf = "clientes.pdf"
    pdf = SimpleDocTemplate(nombre_pdf, pagesize=landscape(letter))

    # Crear tabla
    tabla = Table(contenido)
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Fondo gris para cabecera
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Texto blanco para cabecera
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación centrada
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fuente en negrita para cabecera
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),  # Espaciado en cabecera
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Fondo beige para datos
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Líneas de la tabla
    ]))

    # Agregar la tabla al PDF
    elementos = [tabla]
    pdf.build(elementos)

    # Abrir el PDF generado
    os.startfile(nombre_pdf)  # En Windows
    # En MacOS/Linux puedes usar `os.system(f"open {nombre_pdf}")


#-----------------------------------------------------------#
#Función con las opciones del CRUD para cualquier entidad   #
#-----------------------------------------------------------#
def menuActualizar(  ):
    titulo = "SELECCIONAR LA OPCIÓN A ACTUALIZAR"
    print(tabulate([['' + Fore.GREEN + "ALMACÉN MARKET \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  Nro. Identificación  "],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  Nombre:    "],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  Fecha Nacimiento "],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  Dirección"],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  Teléfonos  "],
                     ["\t" + Back.YELLOW + "[6]" + Style.RESET_ALL + "  Mail  "],
                     ["\t" + Back.YELLOW + "[7]" + Style.RESET_ALL + "  Estado  "],
                     ["\t" + Back.YELLOW + "[8]" + Style.RESET_ALL + "  Regresar     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))
    
def actualizar ( encabezado, cliente ):        
    while True:                
        print("*** ACTUALIZANDO DATOS DEL CLIENTE ***")
        print("*" * 30)    
        libreria.mostrar(encabezado, cliente)
        menuActualizar()
        respuesta = libreria.LeerCaracter("OPCION: ")
        match respuesta:
            case '1':
                cliente[1] = libreria.leerCadena( "NRO. Identificación: ", 20 ).upper() #input("NRO. IDENTIFICACIÓN: ")
            case '2':
                cliente[2] = libreria.leerCadena( "Nombre ", 100 ).title()        #input("NOMBRE: ")
            case '3':
                cliente[3] = libreria.leerFecha("Fecha Nacimiento (YYYY-MM-DD): ")
            case '4':
                cliente[4] = libreria.leerCadena("Dirección: ", 100) #input("DIRECCIÓN: ")
            case '5':
                cliente[5] = libreria.leerCadena("Teléfonos: ", 50)
            case '6':
                cliente[6] = libreria.leerMail("Mail: ")
            case '7':
                cliente[7] = libreria.leerDiccionario(diccionarioEstados, "Estado: ")
            case '8':
                return cliente
            case _:
                libreria.mensajeErrorEsperaSegundos("OPCIÓN NO VALIDA", 1)    
    

def insertar ( codigo ):
    libreria.limpiarPantalla()
    print("*** INSERTAR CLIENTE ***")
    print("*" * 30)
    print(f"CÓDIGO: {codigo}")
    identificacion  = libreria.leerCadena( "NRO. Identificación: ", 20 ).upper() #input("NRO. IDENTIFICACIÓN: ")
    nombres         = libreria.leerCadena( "Nombre: ", 100 ).title()        #input("NOMBRE: ")
    fechaNacimiento = libreria.leerFecha("Fecha Nacimiento (YYYY-MM-DD): ")
    direccion       = libreria.leerCadena("Dirección: ", 100) #input("DIRECCIÓN: ")
    telefonos       = libreria.leerCadena("Teléfonos: ", 50)
    mail            = libreria.leerMail("MAIL: ")
    estado = 'A'
    #indices respetar 0         1            2           3              4          5        6     7
    cliente     = [codigo, identificacion, nombres, fechaNacimiento, direccion, telefonos, mail, estado]
    return cliente

#VARIABLES GLOBALES Y CONSTANTES
rutaDirectorio = "datos/"
nombreArchivo   = os.path.join(rutaDirectorio, 'clientes.dat')
#nombreArchivo   = "clientes.dat"

diccionarioEstados = {
    'A': "Activa",
    'I': "Inactivo"
}

#ESTRUCTURAS DE DATOS A UTILIZAR 
cliente    = []  #Lista una solo cliente
clientes   = []  #Lista de Listas, muchos clientes
encabezado = [Fore.GREEN + Style.BRIGHT + "Código", "Identificación", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail", "Estado" + Style.RESET_ALL]

clientes = libreria.cargar(clientes, nombreArchivo)

#INICIO DEL PROGRAMA
while True:
    libreria.menuCrud( "GESTION CLIENTES" )
    #opcion = input("OPCION: ")[0]
    opcion = libreria.LeerCaracter("OPCION: ")
    match opcion:
        case '1':            
            codigoBuscar = input("CÓDIGO: ").strip().upper()
            posicion = libreria.buscar(clientes, codigoBuscar)
            mensaje = "❌ YA EXISTE NO SE PERMITEN DUPLICADOS " + codigoBuscar
            if (posicion < 0):
                cliente = insertar( codigoBuscar )
                clientes.append(cliente)
                libreria.guardar(clientes, nombreArchivo)
                mensaje = "\U00002705 INSERTADO CORRECTAMENTE"
            libreria.mensajeEsperaSegundos( mensaje, 2 )
        case '2':            
            mensaje = " SIN INFORMACIÓN PARA LISTAR "
            if (clientes):
                libreria.listar(encabezado, clientes)
                respuesta = libreria.LeerCaracter("Imprimir PDF (Si-No)").upper()
                if respuesta == 'S':
                    generarPDF (encabezado, clientes)
                mensaje = "\U00002705 FIN DE LISTAR <ENTER> Continuar"
            libreria.mensajeEsperaEnter( mensaje )
        case '3':           
            mensaje = " SIN INFORMACIÓN PARA CONSULTAR "
            if (clientes):            
                codigoBuscar = input("CÓDIGO: ").strip().upper()
                posicion = libreria.buscar(clientes, codigoBuscar)
                mensaje = "\u26A0 NO EXISTE EL REGISTRO " + codigoBuscar
                if (posicion >= 0):
                    cliente = clientes[posicion]
                    libreria.mostrar(encabezado, cliente)
                    mensaje = "\U00002705 FIN DE CONSULTAR <ENTER> Continuar"            
            libreria.mensajeEsperaEnter( mensaje )
        case '4':          
            mensaje = " SIN INFORMACIÓN PARA ACTUALIZAR "
            if (clientes):            
                codigoBuscar = input("CÓDIGO: ").strip().upper()
                posicion = libreria.buscar(clientes, codigoBuscar)
                mensaje = "\u26A0 NO EXISTE EL REGISTRO " + codigoBuscar
                if (posicion >= 0):
                    cliente = clientes[posicion]
                    cliente = actualizar (encabezado, cliente)    #retornar el registro actualizado
                    clientes[posicion] = cliente
                    libreria.guardar(clientes, nombreArchivo) 
                    mensaje = "\U00002705 FIN DE ACTUALIZAR <ENTER> Continuar"            
            libreria.mensajeEsperaEnter( mensaje )
        case '5':          
            mensaje = " SIN INFORMACIÓN PARA ELIMINAR "
            if (clientes):            
                codigoBuscar = input("CÓDIGO: ").strip().upper()
                posicion = libreria.buscar(clientes, codigoBuscar)
                mensaje = "\u26A0 NO EXISTE EL REGISTRO " + codigoBuscar
                if (posicion >= 0):
                    cliente = clientes[posicion]
                    libreria.mostrar(encabezado, cliente)
                    mensaje = "\U00002705 NO ELIMINADO - FIN DE ELIMINAR <ENTER> Continuar"                     
                    respuesta = libreria.LeerCaracter("Seguro de Eliminar (Sí - No): ")
                    if (respuesta.lower() == 's'):
                        clientes.remove(clientes[posicion])     #o también con    del clientes[posicion] 
                        libreria.guardar(clientes, nombreArchivo)                   
                        mensaje = "\U00002705 REGISTRO ELIMINADO - FIN DE ELIMINAR <ENTER> Continuar"  
            libreria.mensajeEsperaSegundos( mensaje, 2 )
        case '6':
            print("SALE DEL PROGRAMA ") #insertar()
            libreria.mensajeEsperaSegundos( "INSERTADO", 1 )
            break
        case _:
            libreria.mensajeEsperaSegundos( "OPCION NO VALIDA", 1 )
            libreria.limpiarPantalla()