# CRISTIAN ARMANDO LARIOS BRAVO
# HACIENDO Y PROBANDO CODIGOS CHIDOS

#Importacion de librerias
import os
import time
from Funciones_Automatas.automatas import *
from Funciones_Automatas.menuAutomatas import Automatas
from Funciones_Gramaticas.gramaticas import *
from Funciones_Gramaticas.menuGramaticas import Gramaticas


# main
def main():
    while True:
        try:
            os.system("cls")
            # menu con opciones
            print("####### PROGRAMA DE AUTOMATAS Y GRAMATICAS #######")
            print("1.- Automatas\n2.- Gramaticas\n3.- Salir")
            opc = str(input("Introduce la opcion => "))
            if opc == "1":
                if Automatas():
                    break
            elif opc == "2":
                if Gramaticas():
                    break
            elif opc == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion equivocada")
                time.sleep(3)
                os.system("cls")
        except:
            print("No va a tronar mi codigo:)")

if __name__ == "__main__":
    main()