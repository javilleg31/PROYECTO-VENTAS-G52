

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import libreria
import os

from tabulate import tabulate
from colorama import Fore, Back, Style, init


def histogramaVentasProductos (datos, encabezadoDetalle, columna_producto, columna_total):
  df = pd.DataFrame(datos, columns=encabezadoDetalle)

  # Agrupar por 'Factura' y sumar el 'TotalPagar'
  ventas_por_producto = df.groupby(columna_producto)[columna_total].sum()

  # Graficar el histograma
  ventas_por_producto.plot(kind='bar')

  # Graficar el histograma con colores aleatorios
  colors = np.random.rand(len(ventas_por_producto), 3)
  bars = plt.bar(ventas_por_producto.index, ventas_por_producto.values, color=colors)

  # Añadir los valores encima de las barras
  for bar in bars:        
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2 - 0.15, yval + 10, round(yval, 2))

  # Configurar etiquetas y título
  plt.xlabel('Productos')
  plt.ylabel('Total Ventas')
  plt.title('Ventas por Producto')

  # Inclinación de las etiquetas del eje x a 45 grados
  plt.xticks(rotation=45)

  # Mostrar el gráfico
  plt.show()


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)

def pastelVentasVendedor (datos, encabezadoFactura, columna_vendedor, columna_total):
  df = pd.DataFrame(datos, columns=encabezadoFactura)  #convertir la lista de listas a DataFrame

  # Agrupar por 'Vendedor' y sumar el 'TotalPagar'
  ventas_por_vendedor = df.groupby(columna_vendedor)[columna_total].sum()

  # Graficar el pastel con colores aleatorios
  colors = np.random.rand(len(ventas_por_vendedor), 3)
  ventas_por_vendedor.plot(kind='pie', autopct=lambda pct: func(pct, ventas_por_vendedor.values), colors=colors)

  # Configurar título
  plt.title('Ventas por Factura')

  # Mostrar el gráfico
  plt.show()
  
  
def histogramaVentasFacturas (datos, encabezadoFactura, columna_factura, columna_total):
  df = pd.DataFrame(datos, columns=encabezadoFactura)

  # Agrupar por 'Factura' y sumar el 'TotalPagar'
  ventas_por_factura = df.groupby(columna_factura)[columna_total].sum()

  # Graficar el histograma
  ventas_por_factura.plot(kind='bar')

  # Graficar el histograma con colores aleatorios
  colors = np.random.rand(len(ventas_por_factura), 3)
  bars = plt.bar(ventas_por_factura.index, ventas_por_factura.values, color=colors)

  # Añadir los valores encima de las barras
  for bar in bars:        
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2 - 0.15, yval + 10, round(yval, 2))

  # Configurar etiquetas y título
  plt.xlabel('Factura')
  plt.ylabel('Total Ventas')
  plt.title('Ventas por Factura')

  # Inclinación de las etiquetas del eje x a 45 grados
  plt.xticks(rotation=45)

  # Mostrar el gráfico
  plt.show()
  

def menuReportes(  ): 
    titulo = "***** MENU PRINCIPAL ****"
    libreria.limpiarPantalla()    #os.system('cls')
    print(tabulate([['' + Fore.GREEN + "ALMACÉN MARKET \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  HISTOGRAMA VENTAS X FACTURAS"],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  HISTOGRAMA VENTAS X PRODUCTO"],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  PASTEL VENTAS X VENDEDOR"],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  LINEAS VENTAS X VENDEDOR"],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  SALIR     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))
    

#ESTRUCTURAS DE DATOS A UTILIZAR 
factura    = []  #Lista una solo vendedor
facturas   = []  #Lista de Listas, muchos vendedores
encabezadoFactura = ["Factura", "Vendedor", "Cliente", "Fecha", "Forma Pago", "Estado", "Total IVA", "Total Descuentos", "TotalFactura"]

#ESTRUCTURAS DE DATOS productos 
encabezadoDetalle = ['Factura', 'Código Producto', 'Precio Unitario', 'Cantidad', 'IVA', 'Descuento', 'TotalProducto']
detalle  = []
detalles = []

rutaDirectorio = "datos/"
nombreArchivoFacturas   = os.path.join(rutaDirectorio, 'facturas.dat')
nombreArchivoDetalles   = os.path.join(rutaDirectorio, 'detalles.dat')

facturas   = libreria.cargar(facturas, nombreArchivoFacturas)
detalles   = libreria.cargar(detalles, nombreArchivoDetalles)

def menu():
    if detalles is not None:
        while True:
            menuReportes()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                histogramaVentasFacturas (facturas, encabezadoFactura, 'Factura', 'TotalFactura')
                #histogramaPorFacturas (detalles, encabezadoDetalle)
            elif opcion == '2':
                histogramaVentasProductos (detalles, encabezadoDetalle, 'Código Producto', 'TotalProducto')
            elif opcion == '3':                
                pastelVentasVendedor (facturas, encabezadoFactura, 'Vendedor', 'TotalFactura')
            elif opcion == '4':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
