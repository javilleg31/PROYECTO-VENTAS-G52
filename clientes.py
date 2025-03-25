import libreria
import os
from colorama import Fore, Back, Style, init
init()

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
    #indices respetar 0         1            2           3              4          5        6
    cliente     = [codigo, identificacion, nombres, fechaNacimiento, direccion, telefonos, mail]
    return cliente

#VARIABLES GLOBALES Y CONSTANTES
rutaDirectorio = "datos/"
nombreArchivo   = os.path.join(rutaDirectorio, 'clientes.dat')
#nombreArchivo   = "clientes.dat"

#ESTRUCTURAS DE DATOS A UTILIZAR 
cliente    = []  #Lista una solo cliente
clientes   = []  #Lista de Listas, muchos clientes
encabezado = [Fore.GREEN + Style.BRIGHT + "Código", "Identificación", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail" + Style.RESET_ALL]

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
            print("LLAMADO A LA FUNCION ACTUALIZAR") #actualizar()
            libreria.mensajeEsperaSegundos( "INSERTADO", 1 )
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
                        mensaje = "\U00002705 REGISTRO ELIMINADO - FIN DE ELIMINAR <ENTER> Continuar"  
            libreria.mensajeEsperaSegundos( mensaje, 2 )
        case '6':
            print("SALE DEL PROGRAMA ") #insertar()
            libreria.mensajeEsperaSegundos( "INSERTADO", 1 )
            break
        case _:
            libreria.mensajeEsperaSegundos( "OPCION NO VALIDA", 1 )
            libreria.limpiarPantalla()