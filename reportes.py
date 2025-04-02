

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import libreria
import os

'''
def graficar_histograma(datos, columna_factura, columna_total):
  df = pd.DataFrame(datos, columns=['Factura', 'Total'])
  fig, ax = plt.subplots(1, 2, figsize=(12, 6))

  # Histograma de Producción de Energía
  df.groupby(columna_factura)[columna_total].sum().plot(kind='bar', ax=ax[0], color='skyblue', edgecolor='black')
  ax[0].set_title('VENTAS POR FACTURA')
  ax[0].set_xlabel('Facturas')
  ax[0].set_ylabel('Total Ventas')
  ax[0].grid(axis='y', linestyle='--', alpha=0.7)

  # Colocar valores encima de las barras de producción
  for barra in ax[0].patches:
    ax[0].annotate(f'{barra.get_height():.0f}',
           (barra.get_x() + barra.get_width() / 2, barra.get_height()),
           ha='center', va='bottom')    
   
  plt.tight_layout()
  plt.show()
'''

def histogramaPorFacturas (detalles, encabezadoDetalle):
    #encabezadoDetalle = ['Nro.Factura', 'Código Producto', 'Precio Unitario', 'Cantidad', 'IVA', 'Descuento', 'total']
    df = pd.DataFrame (detalles, columns=encabezadoDetalle)

    ventas_por_factura = df.groupby('Nro.Factura')['total'].sum()

    ventas_por_factura.plot(kind='bar')

    plt.xlabel('FACTURAS')
    plt.ylabel('Ventas x miles')
    plt.title('VENTRAS X FACTURA')

    plt.show()


#ESTRUCTURAS DE DATOS productos 
encabezadoDetalle = ['Nro.Factura', 'Código Producto', 'Precio Unitario', 'Cantidad', 'IVA', 'Descuento', 'total']
detalle  = []
detalles = []

rutaDirectorio = "datos/"
nombreArchivoDetalles   = os.path.join(rutaDirectorio, 'detalles.dat')

detalles   = libreria.cargar(detalles, nombreArchivoDetalles)

def menu():
    if detalles is not None:
        while True:
            print("\nMenú de Gráficas")
            print("1. Histogramas Facturas")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                histogramaPorFacturas (detalles, encabezadoDetalle)
            elif opcion == '2':
                break
            elif opcion == '3':
                break
            elif opcion == '4':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
