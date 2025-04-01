

from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image, Paragraph
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

import libreria
import os
import sys
from datetime import date
from tabulate import tabulate
from colorama import Fore, Back, Style, init
init()

# Función para generar el PDF
def generar_pdf_factura(factura_info, cliente_info, detalle_factura):
    directorio = "reportesPDF"
    archivo_pdf = os.path.join(directorio, "factura.pdf") 

    #archivo_pdf = "Factura.pdf"
    doc = SimpleDocTemplate(archivo_pdf, pagesize=landscape(letter),
                            leftMargin=30, rightMargin=30,
                            topMargin=30, bottomMargin=30)
    elementos = []

    # Agregar el logo en la parte superior derecha
    logo_path = "imagenes/logo.jpg"  # Asegúrate de que el archivo existe en la misma carpeta
    try:
        logo = Image(logo_path, width=1.5 * inch, height=0.7 * inch)
        logo.hAlign = 'RIGHT'
        elementos.append(logo)
    except:
        print("⚠️ No se encontró el logo. Se generará sin él.")

    # Espaciado después del logo
    elementos.append(Spacer(1, 10))

    # Agregar título de la factura
    estilo = getSampleStyleSheet()
    titulo = Paragraph("<b>FACTURA DE VENTA</b>", estilo["Title"])
    elementos.append(titulo)
    elementos.append(Spacer(1, 12))

    # Sección: Datos de la Factura
    tabla_factura = Table([factura_info], colWidths=[120, 200])
    tabla_factura.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elementos.append(tabla_factura)
    elementos.append(Spacer(1, 12))

    # Sección: Datos del Cliente
    tabla_cliente = Table([cliente_info], colWidths=[120, 300])
    tabla_cliente.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elementos.append(tabla_cliente)
    elementos.append(Spacer(1, 12))

    # Sección: Detalle de la Factura
    tabla_detalle = Table(detalle_factura, colWidths=[100, 120, 120, 60, 80, 120])
    tabla_detalle.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elementos.append(tabla_detalle)

    # Generar el PDF
    doc.build(elementos)
    print(f"✅ PDF generado correctamente: {archivo_pdf}")

# Función para consultar la factura por su número
def armarDetallesFactura (numeroFactura, detalles):
    detallesAux = []
    for indice, registro in enumerate(detalles):   #recorre toda la lista y extrae registro a registro con su indice
        if str(registro[0]).upper() == str(numeroFactura).upper():
            detallesAux.append(registro)
    return detallesAux

def mostrarFacturaCompleta(encabezadoFactura, encabezadoDetalle, listaFactura, listaDetalles): 
    os.system('cls')
    # Formatear columnas de numeros que no salga exponencial
    lista = [listaFactura]   #CONVERTIMOS A LISTA DE LISTAS POR QUE TABULATE LO EXIGE
    #headers = encabezado; #dependiendo de la entidad, se envian por parametro
    print (Fore.YELLOW + "******** CABECERA DE LA FACTURA DE VENTA ********" + Style.RESET_ALL)
    print(tabulate(
                   lista,
                   headers = encabezadoFactura,
                   tablefmt='fancy_grid',
                   stralign='left',
                   floatfmt=",.0f")
                   )
    
    print (Fore.YELLOW + "******** DETALLE DE LA FACTURA ********" + Style.RESET_ALL)
    print(tabulate(listaDetalles,
                   headers = encabezadoDetalle,
                   tablefmt='fancy_grid',
                   stralign='left',
                   floatfmt=",.0f"))
    
def actualizarExistenciasProducto (detallesEstaFactura, productos):  
    #global productos     
    for productoEstaFactura in detallesEstaFactura:
        codigoProducto  = productoEstaFactura[1] 
        cantidadVendida = productoEstaFactura[3]
        posicion = libreria.buscar(productos, codigoProducto)
        producto = productos[posicion]
        producto[3] = producto[3] - cantidadVendida   #resto de las existencias
        productos[posicion] = producto
    return productos

         

def venderProductos ( numeroFactura, productos ):
    detalleEstaFactura  = []
    detallesEstaFactura = []
    #             0         1           2                  3           4        5           
    #PRODUCTO['Código', 'Nombre', 'Precio Unitario', 'Existencias', 'IVA', 'Descuento', 'estado', 'Fecha Vencimiento']
    #DETALLE ['Nro.Factura', 'Código Producto', 'Precio Unitario', 'Cantidad', 'IVA', 'Descuento', 'total']
    while True:
        print("*** DETALLE DE LA FACTURA ", numeroFactura)
        #libreria.mostrar(encabezado, factura)
        codigoProducto, posicionProducto = libreria.leerCodigoValidado(productos, "Código Producto: ")
        producto = productos[posicionProducto]
        print(f"Nombre: {producto[1]} Precio Unitario: {producto[2]} Existencias: {producto[3]} IVA: {producto[4]} Descuento: {producto[5]} %")
        #maximo_productos = producto[3]    
        cantidad = libreria.leerEntero("Cantidad: ", 1, producto[3])
        precioUnidad = producto[2]
        pagoIva   = cantidad * precioUnidad * (producto[4] / 100)  #IVA del producto inicial
        descuento = cantidad * precioUnidad * (producto[5] / 100)  #DESCUENTO 
        total     = cantidad * precioUnidad + pagoIva - descuento
        detalleEstaFactura = [numeroFactura, codigoProducto, precioUnidad, cantidad, pagoIva, descuento, total]
        detallesEstaFactura.append (detalleEstaFactura)
        respuesta = libreria.LeerCaracter("Otro Producto (Si-No): ").upper()
        if respuesta != 'S':
            return detallesEstaFactura
    

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
    totalDescuento = 0
    totalFactura = 0
    factura = [numeroFactura, codigoVendedor, codigoCliente, fecha, formaPago, estado, totalIVA, totalDescuento, totalFactura]

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
encabezado = [Fore.GREEN + Style.BRIGHT + "NRO.Factura", "Vendedor", "Cliente", "Fecha", "Forma Pago", "Estado", "Total IVA", "Total Descuentos", "Total Factura" + Style.RESET_ALL]

#ESTRUCTURAS DE DATOS productos 
encabezadoDetalle = ['Nro.Factura', 'Código Producto', 'Precio Unitario', 'Cantidad', 'IVA', 'Descuento', 'total']
detalle  = []
detalles = []


#estructuras para el cliente
cliente    = []  #Lista una solo cliente
clientes   = []  #Lista de Listas, muchos clientes
encabezadoCliente = [Fore.GREEN + Style.BRIGHT + "Código", "Identificación", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail", "Estado" + Style.RESET_ALL]

#ESTRUCTURAS DE DATOS vendedores 
vendedor    = []  #Lista una solo vendedor
vendedores   = []  #Lista de Listas, muchos vendedores
encabezadoVendedor = [Fore.GREEN + Style.BRIGHT + "Código", "Identificación", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail", "Estado", "Salario" + Style.RESET_ALL]

#ESTRUCTURAS DE DATOS productos 
encabezadoProducto = ['Código', 'Nombre', 'Precio Unitario', 'Existencias', 'IVA', 'Descuento', 'estado', 'Fecha Vencimiento']
producto  = []
productos = []

rutaDirectorio = "datos/"
nombreArchivo   = os.path.join(rutaDirectorio, 'facturas.dat')
nombreArchivoCliente   = os.path.join(rutaDirectorio, 'clientes.dat')
nombreArchivoVendedor  = os.path.join(rutaDirectorio, 'vendedores.dat')
nombreArchivoProductos = os.path.join(rutaDirectorio, 'productos.dat')
nombreArchivoDetalles  = os.path.join(rutaDirectorio, 'detalles.dat')

facturas   = libreria.cargar(facturas, nombreArchivo)
clientes   = libreria.cargar(clientes, nombreArchivoCliente)
vendedores = libreria.cargar(vendedores, nombreArchivoVendedor)
productos  = libreria.cargar(productos, nombreArchivoProductos)
detalles   = libreria.cargar(detalles, nombreArchivoDetalles)

directorio_pdf = "reportesPDF"
archivo_pdf = os.path.join(directorio_pdf, "factura.pdf")

#INICIO DEL PROGRAMA
def menu():
    while True:
        libreria.menuCrud( "GESTION FACTURAS" )
        #opcion = input("OPCION: ")[0]
        opcion = libreria.LeerCaracter("OPCION: ")
        match opcion:
            case '1': 
                global productos
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
                            #construir el datalle de la factura
                            detallesEstaFactura = venderProductos ( facturaBuscar, productos )  #factura[0]
                            if detallesEstaFactura:
                                #solamente se guarda la factura si tiene productos vendidos
                                factura[6] = sum( fila[4]  for fila in detallesEstaFactura)   #total iva
                                factura[7] = sum( fila[5]  for fila in detallesEstaFactura)   #Total descuento
                                factura[8] = sum( fila[6]  for fila in detallesEstaFactura)   #totalFactura
                                facturas.append(factura)
                                mensaje = "FACTURA CREADA"
                                libreria.guardar(facturas, nombreArchivo)
                                for detalle in detallesEstaFactura:
                                    detalles.append(detalle)
                                libreria.guardar(detalles, nombreArchivoDetalles)
                                productos = actualizarExistenciasProducto (detallesEstaFactura, productos)
                                libreria.guardar(productos, nombreArchivoProductos)
                                mostrarFacturaCompleta(encabezado, encabezadoDetalle, factura, detallesEstaFactura)
                                input()
                libreria.mensajeErrorEsperaSegundos(mensaje, 1)
            case '2': 
                mensaje = "AVISO: SIN FACTURAS PARA LISTAR"
                if (facturas):
                    libreria.listar(encabezado, facturas)
                    mensaje = "FIN DE LISTAR"
                libreria.mensajeEsperaEnter(mensaje)
            case '3': #USUARIO SELECCIONA CONSULTAR
                codigoBuscar = input("\n\nCODIGO A CONSULTAR: ").upper()
                encontrado = libreria.buscar(facturas, codigoBuscar)
                mensaje = "NO SE ENCUENTRA"
                if  encontrado >= 0:
                    factura = facturas[encontrado]                    
                    detallesEstaFactura = armarDetallesFactura(codigoBuscar, detalles)
                    mostrarFacturaCompleta(encabezado, encabezadoDetalle, factura, detallesEstaFactura)
                    respuesta = libreria.LeerCaracter("Imprimir PDF (SÍ-NO): ").upper()
                    if respuesta == 'S':
                        #anchoColumnas = [60, 70, 125, 100, 100, 100, 120, 50]
                        posicionCliente = libreria.buscar(clientes, factura[2])
                        cliente = clientes[posicionCliente]
                        generar_pdf_factura(factura, cliente, detallesEstaFactura)
                        libreria.abrirPDF (archivo_pdf)

                    mensaje = ">><FIN DE CONSULTAR >>>"

                libreria.mensajeEsperaEnter("Continuar <ENTER>")
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