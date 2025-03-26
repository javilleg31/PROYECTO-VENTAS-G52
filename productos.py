import os
import libreria

#FUNCINES PROPIAS
def menuActualizar():
    print("[1] Nombre")
    print("[2] Precio Unidad")
    print("[3] Existencias")
    print("[4] IVA")
    print("[5] DESCUENTO")
    print("[6] ESTADO")
    print("[7] FECHA VENCIMIENTO")
    print("[8] REGRESAR")


def actualizar(encabezado, producto):
    #[codigo, nombre, precioUnitario, existencias, iva, descuento, estado, fecha]
    while True:
        libreria.mostrar(encabezado, producto)
        print("*** ACTUALIZANDO DATOS DEL PRODUCTO ***")
        print("*" * 30)
        menuActualizar()
        respuesta   = libreria.LeerCaracter("OPCIÓN: ")
        match respuesta:
            case '1':
                producto[1] = libreria.leerCadena("Nombre: ", 100)
            case '2':
                producto[2] = libreria.leerEntero("Precio Unidad:" , 1, 10000000)
            case '3':
                producto[3] = libreria.leerEntero("Existencias:" , 1, 1000)
            case '4':
                producto[4] = libreria.leerEntero("IVA:", 0, MAXIMO_IVA)
            case '5':
                producto[5] = libreria.leerEntero("Descuento(%): ", 0, 50)
            case '6':
                producto[6] = 'A'
            case '7':
                producto[7] = libreria.leerFecha("Fecha Vencimiento (YYYY-MM-DD): ")
            case '8':
                return producto
            case _:
                libreria.mensajeErrorEsperaSegundos("OPCION NO VALIDA", 1)
          


def insertar( codigo ):
    libreria.limpiarPantalla()
    print("*** INSERTAR CLIENTE ***")
    print("*" * 30)
    #codigo         = libreria.leerCadena("Código: ", 10)
    print("Código: ", codigo)
    nombre         = libreria.leerCadena("Nombre: ", 100)
    precioUnitario = libreria.leerEntero("Precio Unidad:" , 1, 10000000)
    existencias    = libreria.leerEntero("Existencias:" , 1, 1000)
    iva            = libreria.leerEntero("IVA:", 0, MAXIMO_IVA)
    descuento      = libreria.leerEntero("Descuento(%): ", 0, 50)
    estado         = 'A'
    fecha          = libreria.leerFecha("Fecha Vencimiento (YYYY-MM-DD): ")

    producto = [codigo, nombre, precioUnitario, existencias, iva, descuento, estado, fecha]
    return producto



#VARIABLES GLOBALES
MAXIMO_IVA = 20
encabezado = ['Código', 'Nombre', 'Precio Unitario', 'Existencias', 'IVA', 'Descuento', 'estado', 'Fecha Vencimiento']
producto  = []
productos = []

rutaDirectorio = "datos/"
nombreArchivo   = os.path.join(rutaDirectorio, 'productos.dat')

productos = libreria.cargar(productos, nombreArchivo)

while True:
    libreria.menuCrud( "PRODUCTOS" )
    opcion = libreria.LeerCaracter("OPCIÓN:")
    match opcion:
        case '1':
            codigoBuscar = libreria.leerCadena("Código:", 10).upper()
            posicion = libreria.buscar(productos, codigoBuscar)
            mensaje = "NO SE PERMITE DUPLICADOS " + codigoBuscar
            if (posicion < 0):
                producto = insertar( codigoBuscar )
                productos.append(producto)
                libreria.guardar(productos, nombreArchivo)
                mensaje = "INSERTADO CORRECTAMENTE "
            libreria.mensajeErrorEsperaSegundos(mensaje, 1)
        case '2':
            mensaje = "SIN REGISTROS PARA MOSTRAR " 
            if (productos):
                libreria.listar(encabezado, productos)
                mensaje = "FIN DE LISTAR " 
            libreria.mensajeEsperaEnter( mensaje )
        case '3':
            mensaje = "SIN REGISTROS PARA MOSTRAR " 
            if (productos):
                codigoBuscar = libreria.leerCadena("Código:", 10)
                posicion = libreria.buscar(productos, codigoBuscar)
                mensaje = "NO SE ENCONTRADO " + codigoBuscar
                if (posicion >= 0):
                    producto = productos[posicion]
                    libreria.mostrar(encabezado, producto)
                    mensaje = "FIN DE CONSULTAR "
            libreria.mensajeEsperaEnter( mensaje )
        case '4':
            mensaje = "SIN REGISTROS PARA MOSTRAR " 
            if (productos):
                codigoBuscar = libreria.leerCadena("Código:", 10)
                posicion = libreria.buscar(productos, codigoBuscar)
                mensaje = "NO SE ENCONTRADO " + codigoBuscar
                if (posicion >= 0):
                    producto = productos[posicion]
                    producto = actualizar(encabezado, producto)
                    productos[posicion] = producto
                    libreria.guardar(productos, nombreArchivo)
                    #libreria.mostrar(encabezado, producto)
                    mensaje = "FIN DE ACTUALIZAR "
            libreria.mensajeEsperaSegundos( mensaje, 1)
        case '5':
            mensaje = "SIN REGISTROS PARA ELIMINAR " 
            if (productos):
                codigoBuscar = libreria.leerCadena("Código:", 10)
                posicion = libreria.buscar(productos, codigoBuscar)
                mensaje = "NO SE ENCONTRADO " + codigoBuscar
                if (posicion >= 0):
                    producto = productos[posicion]
                    libreria.mostrar(encabezado, producto)
                    respuesta = libreria.LeerCaracter("Seguro de Eliminar (Si-No):")
                    if (respuesta.upper() == 'S'):
                        productos.remove(productos[posicion])                        
                        libreria.guardar(productos, nombreArchivo)
                        mensaje = " REGISTRO ELIMINADO  " + codigoBuscar
            libreria.mensajeEsperaSegundos( mensaje, 1)
        case '6':
            break
        case _:
            print("OPCION NO VALIDA")
        