

import libreria
import os
import sys
from tabulate import tabulate
from colorama import Fore, Back, Style, init

import vendedores as v
import clientes as c
import productos as p
import facturas as f
#-----------------------------------------------------------#
#Función con las opciones del CRUD para cualquier entidad   #
#-----------------------------------------------------------#
def menu(  ): 
    titulo = "***** MENU PRINCIPAL ****"
    libreria.limpiarPantalla()    #os.system('cls')
    print(tabulate([['' + Fore.GREEN + "ALMACÉN MARKET \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  GESTIONAR VENDEDORES  "],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  GESTIONAR CLIENTES    "],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  GESTIONAR PRODUCTOS "],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  GESTIONAR VENTAS"],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  REPORTES  "],
                     ["\t" + Back.YELLOW + "[6]" + Style.RESET_ALL + "  SALIR     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))
    
#PROGRAMA PRINCIPAL PARA NAVEGAR ENTRE OTROS ARCHIVOS
def main():
    while True:
        menu()
        opcion = libreria.LeerCaracter("OPCIÓN: ").upper()
        match opcion:
            case '1':
                v.menu()
            case '2':
                c.menu()
            case '3':
                p.menu()
            case '4':
                f.menu()
            case '5':
                print("llamar a vendedores")
                input()
            case '6':
                libreria.mensajeErrorEsperaSegundos("GRACIAS POR UTILIZARNOS", 1)
                libreria.limpiarPantalla()
                sys.exit()

if __name__ == "__main__":
    main()