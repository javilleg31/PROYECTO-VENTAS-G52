

import libreria
import os
import sys
from datetime import date
from tabulate import tabulate
from colorama import Fore, Back, Style, init
init()

def insertar ( numeroFactura, codigoCliente, codigoVendedor ):
    libreria.limpiarPantalla()
    print("*** NUEVA FACTURA ***")
    print("*" * 30)
    print(f"Nro, Factura: {numeroFactura}")
    #pedimos el resto de datos    
    #vendedor   = libreria.leerCadena("Código Vendedor: ", 10).upper()
    #cliente    = libreria.leerCadena("Código Cliente: ", 10).upper()
    fecha      = str(date.today()) 
    formaPago  = libreria.leerDiccionario (diccionarioFormaPagos, "Forma de Pago: ")
    estado     = 'A'
    totalIVA   = 0
    totalFactura = 0
    factura = [numeroFactura, codigoVendedor, codigoCliente, fecha, formaPago, estado, totalIVA, totalFactura]

    return factura

#factura = [numeroFactura, codigoVendedor, codigoCliente, fechaFactura, formaPago, estado, totalIva, totalFactura]
#VARIABLES GLOBALES Y CONSTANTES
diccionarioEstados = {
    'A': "Activa",
    'X': "Anulada",
    'C': "Contabilizada"
}

diccionarioFormaPagos = {
    'E': "Efectivo",
    'D': "Tarjeta Debito",
    'C': "Tarjeta Crédito",
    'T': "Transferencia"
}


#ESTRUCTURAS DE DATOS A UTILIZAR 
factura    = []  #Lista una solo vendedor
facturas   = []  #Lista de Listas, muchos vendedores
encabezado = [Fore.GREEN + Style.BRIGHT + "NRO.Factura", "Vendedor", "Cliente", "Fecha", "Forma Pago", "Estado", "Total IVA", "Total Factura" + Style.RESET_ALL]

#estructuras para el cliente
cliente    = []  #Lista una solo cliente
clientes   = []  #Lista de Listas, muchos clientes
encabezadoCliente = [Fore.GREEN + Style.BRIGHT + "Código", "Identificación", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail", "Estado" + Style.RESET_ALL]

#ESTRUCTURAS DE DATOS vendedores 
vendedor    = []  #Lista una solo vendedor
vendedores   = []  #Lista de Listas, muchos vendedores
encabezadoVendedor = [Fore.GREEN + Style.BRIGHT + "Código", "Identificación", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail", "Estado", "Salario" + Style.RESET_ALL]

rutaDirectorio = "datos/"
nombreArchivo   = os.path.join(rutaDirectorio, 'facturas.dat')
nombreArchivoCliente   = os.path.join(rutaDirectorio, 'clientes.dat')
nombreArchivoVendedor  = os.path.join(rutaDirectorio, 'vendedores.dat')


facturas   = libreria.cargar(facturas, nombreArchivo)
clientes   = libreria.cargar(clientes, nombreArchivoCliente)
vendedores = libreria.cargar(vendedores, nombreArchivoVendedor)

#INICIO DEL PROGRAMA
def menu():
    while True:
        libreria.menuCrud( "GESTION FACTURAS" )
        #opcion = input("OPCION: ")[0]
        opcion = libreria.LeerCaracter("OPCION: ")
        match opcion:
            case '1': 
                codigoCliente, posicionCliente = libreria.leerCodigoValidado(clientes, "Código Cliente: ")
                #posicionCliente = libreria.buscar(clientes, codigoCliente)
                mensaje = "ERROR: CLIENTE NO EXISTE"
                if posicionCliente >= 0:
                    cliente = clientes[posicionCliente]
                    print(f"{cliente[1]} \t {cliente[2]}")
                    codigoVendedor, posicionVendedor = libreria.leerCodigoValidado(vendedores, "Código Vendedor: ")
                    #posicionVendedor = libreria.buscar(vendedores, codigoVendedor)
                    mensaje = "ERROR: VENDEDOR NO EXISTE"
                    if posicionVendedor >= 0:                        
                        vendedor = vendedores[posicionVendedor]
                        print(f"{vendedor[1]} \t {vendedor[2]}")
                        facturaBuscar = libreria.leerCadena("Nro. Factura: ", 10).upper()
                        posicion = libreria.buscar(facturas, facturaBuscar)
                        mensaje = "ERROR: FACTURA DUPLICADA"
                        if (posicion < 0):
                            factura = insertar( facturaBuscar, codigoCliente, codigoVendedor)
                            facturas.append(factura)
                            mensaje = "FACTURA CREADA"
                            libreria.guardar(facturas, nombreArchivo)
                libreria.mensajeErrorEsperaSegundos(mensaje, 1)
            case '2': 
                mensaje = "AVISO: SIN FACTURAS PARA LISTAR"
                if (facturas):
                    libreria.listar(encabezado, facturas)
                    mensaje = "FIN DE LISTAR"
                libreria.mensajeEsperaEnter(mensaje)
            case '3':  
                input()
            case '4':
                input()
            case '5': 
                input()
            case '6':
                libreria.mensajeEsperaSegundos( "FINAL ", 1 )
                break
            case _:
                libreria.mensajeEsperaSegundos( "OPCION NO VALIDA", 1 )
                libreria.limpiarPantalla()

if __name__ == "__main__":
    menu()