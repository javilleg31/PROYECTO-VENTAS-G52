import os
import time
from tabulate import tabulate
from colorama import Fore, Back, Style, init
import re
import pickle
from datetime import datetime

init()

import time 
import msvcrt

#función lee un solo carácter NO espera ENTER
def LeerCaracter (mensaje):
  print(mensaje, end="", flush=True)
  return msvcrt.getch().lower().decode('utf-8')  #getch captura un solo caracter No hay que dar enter

##############################################################################################
# Función que valida el ingreso de una cadena que no sea vacia y limitar un maximo caracteres#
##############################################################################################
def leerCadena( mensaje, maximoCaracteres ):
    while True:
        #print(f"{mensaje}", end="", flush=True)
        cadena = input( f"{mensaje} (Máx. {maximoCaracteres} caracteres): ").strip()
        if 0 < len(cadena) <= maximoCaracteres:  #Retorna la cadena válida
           return cadena
        else:
            print(f"❌ Error: La cadena no debe estar vacía y debe tener máximo {maximoCaracteres} caracteres.", end="", flush=True)
            time.sleep(1)                 # Pausa breve de 1 segundo)
            print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
            print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
            continue
        
############################################################################
# Función que valida el ingreso de la fecha en un formatro y rango correcto#
############################################################################
def leerFecha( mensaje ):
    while True:
        #print(f"{mensaje}", end="", flush=True)
        fecha_str = input( mensaje )
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha.strftime("%Y-%m-%d")  #fecha  # Retorna un objeto datetime (fecha y hora)
        except ValueError:
            print("❌ Error: Formato incorrecto. Intente de nuevo.", end="", flush=True)
            time.sleep(1)                 # Pausa breve de 1 segundo)
            print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
            print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
            continue

############################################################################
# Función que valida el ingreso del mail en un formatro correcto           #
############################################################################
def leerMail ( mensaje ):
      while True:
          #print(f"{mensaje}", end="", flush=True) 
          email = input ( mensaje )
          #correo valido verifica antes y despues del @
          patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'          
          if re.match(patron, email.lower()):
            return email
          else:
            print("Error: Email NO es correcto", end="", flush=True)
            time.sleep(1) # Pausa breve de 1 segundo
            print(end="\r\033[K\033[F") # Mueve el cursor al inicio de la linea y limpia la línea

############################################################################
# Función que valida el ingreso de un decimal en un rango minimo y maximo  #
############################################################################
def  leerFlotante (mensaje, minimo, maximo):
  while True:
    print(f"{mensaje} ({minimo}-{maximo}): ", end="", flush=True)
    valor = input().strip().replace(",", ".")
    # Verificar que no esté vacío ni tenga espacios intermedios
    if not valor or " " in valor:
      print(f"❌Error: {mensaje} no debe estar vacío ni contener espacios.", end="", flush=True)
      time.sleep(1)              # Pausa breve de 1 segundo)
      print("\r\033[K", end="")  # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
      continue
    # Verificar si es un número decimal válido
    try:
      numero = float(valor)
      if minimo <= numero <= maximo:  # numero >= minimo and numero <= maximo
        return numero
      else:
        print(f"❌Error: {mensaje} debe estar entre {minimo} y {maximo}.", end="", flush=True)
        time.sleep(1) # Pausa breve de 1 segundo
        print("\r\033[K", end="")       # Mueve cursor al inicio de la línea y limpia la línea
        print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
    except ValueError:
      print("❌Error: {mensaje} inválida. ", end="", flush=True)
      time.sleep(1)                      # Pausa breve de 1 segundo
      print("\r\033[K", end="")       # Mueve cursor al inicio de la línea y limpia la línea
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea

#La función devuelve el nombre del sistema operativo y aplica el comando respectivo
def limpiarPantalla ():    
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')
    
def cabecera ( titulo ): 
    print(Fore.RED + f"\n   {titulo}    \n" + Style.RESET_ALL )


def mensajeEsperaSegundos( mensaje, segundos ):
    print(Fore.YELLOW + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

def mensajeErrorEsperaSegundos( mensaje, segundos ):
    print(Fore.RED + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

##################################################################
# Procedimiento que espera que el usuario presione Enter         #
##################################################################
def mensajeEsperaEnter( mensaje ):
    print("\n" + Fore.GREEN + Style.BRIGHT + mensaje + Style.RESET_ALL, end="")
    input()

#-----------------------------------------------------------#
#Función con las opciones del CRUD para cualquier entidad   #
#-----------------------------------------------------------#
def menuCrud( titulo ): 
    limpiarPantalla()    #os.system('cls')
    print(tabulate([['' + Fore.GREEN + "ALMACÉN MARKET \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  INSERTAR  "],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  LISTAR    "],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  CONSULTAR "],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  ACTUALIZAR"],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  ELIMINAR  "],
                     ["\t" + Back.YELLOW + "[6]" + Style.RESET_ALL + "  SALIR     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))

#----------------------------------------------------------------------------#
#Función para listar cualquier lista, le debo enviar la lista y el encezado  #
#----------------------------------------------------------------------------#
def listar(encabezado, listas): 
    # Formatear columnas de numeros que no salga exponencial
    limpiarPantalla()
    headers = encabezado
    #headers =[Fore.GREEN + 'PLACA', 'MARCA', 'MODELO', 'COLOR', 'PRECIO' ]
    print(tabulate(listas,
                   headers = headers,
                   tablefmt='fancy_grid',
                   stralign='left',
                   floatfmt=",.0f"))

#-----------------------------------------------------------#
# Función para buscar elemento en lista por su codigo PK,   #
# devolver indice si lo encuentra o -1 si no lo encuentra   #
#-----------------------------------------------------------#
def buscar(lista, codigoBuscar):
    posicion = -1
    for indice, registro in enumerate(lista):   #recorre toda la lista y extrae registro a registro con su indice
        #print(indice, " -- ", fila)  0.placa 1.marca 2.color......
        if str(registro[0]).upper() == str(codigoBuscar).upper():
            return indice
    return posicion

#---------------------------------------------------------#
# Función para guardar Información en Archivos - MODO  w, # 
# si existe lo borra, si no existe lo crea                #
#---------------------------------------------------------#
def guardar(lista, filename):
    archivo = open( filename, 'wb') #W se abre solo para escritua y si existe lo borra y crea uno nuevo y B indica que un archivo binario
    pickle.dump(lista, archivo)
    archivo.close()
    print(""+Fore.LIGHTYELLOW_EX+"\n\n>>> Guardando Información en los archivos correspondientes <<< " + Style.RESET_ALL)
    time.sleep(2)

#----------------------------------------------------------------------#
# Función para cargar Información en Archivos, MODO R, de solo lectura #
#----------------------------------------------------------------------#
def cargar(lista, filename):
    try:
        archivo = open(filename, 'rb')   #R se abre solo para lectura y B indica que un archivo binario
        lista = pickle.load(archivo)
        archivo.close()
        print(""+Fore.RED+"\n>>> Cargando Información : "+filename+''+Style.RESET_ALL)
        time.sleep(1)
        return lista
    except:
        print(""+Fore.RED+"\n>>> Error al cargar el archivo o no se ha creado: "+filename+''+Style.RESET_ALL)
        time.sleep(1)
    return lista

