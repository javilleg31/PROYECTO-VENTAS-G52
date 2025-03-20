import libreria
from colorama import Fore, Back, Style, init
init()

def insertar ( codigo ):
    libreria.limpiarPantalla()
    print("*** INSERTAR CLIENTE ***")
    print("*" * 30)
    print(f"CÓDIGO: {codigo}")
    identificacion  = libreria.leerCadena( "NRO. IDENTIFICACIÓN: ", 20 ).upper() #input("NRO. IDENTIFICACIÓN: ")
    nombres         = libreria.leerCadena( "NOMBRE: ", 100 ).capitalize()        #input("NOMBRE: ")
    fechaNacimiento = libreria.leerFecha("FECHA NACIMIENTO (YYYY-MM-DD): ")
    direccion = input("DIRECCIÓN: ")
    telefonos = input("TELEFONOS: ")
    mail = libreria.leerMail("MAIL: ")
    #indices respetar 0        1            2           3              4          5        6
    cliente = [codigo, identificacion, nombres, fechaNacimiento, direccion, telefonos, mail]
    return cliente

#VARIABLES
filename = "clientes.dat"
cliente = []   #Lista una solo vendedor
clientes = []  #Lista de Listas, muchos vendedores
encabezado = [Fore.GREEN + Style.BRIGHT + "Código", "Identificación", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail" + Style.RESET_ALL]

clientes = libreria.cargar(clientes, filename)

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
                libreria.guardar(clientes, filename)
                mensaje = "\U00002705 INSERTADO CORRECTAMENTE"
            libreria.mensajeEsperaSegundos( mensaje, 2 )
        case '2':            
            mensaje = "❌ SIN INFORMACIÓN PARA LISTAR "
            if (clientes):
                libreria.listar(encabezado, clientes)
                mensaje = "\U00002705 FIN DE LISTAR <ENTER> Continuar"
            libreria.mensajeEsperaEnter( mensaje )
        case '3':
            print("LLAMADO A LA FUNCION CONSULTAR") #consultar()
            libreria.mensajeEsperaSegundos( "INSERTADO", 1 )
        case '4':
            print("LLAMADO A LA FUNCION ACTUALIZAR") #actualizar()
            libreria.mensajeEsperaSegundos( "INSERTADO", 1 )
        case '5':
            print("LLAMADO A LA FUNCION ELIMINAR") #eliminar()
            libreria.mensajeEsperaSegundos( "INSERTADO", 1 )
        case '6':
            print("SALE DEL PROGRAMA ") #insertar()
            libreria.mensajeEsperaSegundos( "INSERTADO", 1 )
            break
        case _:
            libreria.mensajeEsperaSegundos( "OPCION NO VALIDA", 1 )
            libreria.limpiarPantalla()