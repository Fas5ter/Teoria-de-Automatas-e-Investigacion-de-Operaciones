# CRISTIAN ARMANDO LARIOS BRAVO
# HACIENDO Y PROBANDO CODIGOS CHIDOS
# METODO COSTO MINIMO CON MODI

import os
import time

from Funciones_CostosMinimos_MODI.Funciones_CostosMinimos_MODI import *

# MAIN
def main():
    while True:
        try:
            n = 30
            # cost_matrix = RegistrarValores(origenes, destinos)
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))

            origenes = Registrar_Val_Origenes()
            destinos = Registrar_Val_Destinos()
            C = crear_matriz(filas, columnas)
            S = RegistrarOfertas(origenes)
            D = RegistrarDemandas(destinos)
            
            S2 = []
            for i in range(len(S)):
                S2.append(S[i])
            D2 = []
            for j in range(len(D)):
                D2.append(D[j])
            
            print("Tabla inicial")
            for e in C:
                print(e)
            print(f"Ofertas: {S}")
            print(f"Demandas: {D}")
            
            print("[ ------------- CARGANDO -------------]")
            for i in range(n + 1):
                time.sleep(0.1)
                print(progress_bar(i, n))
            matriz, total_cost = costoMinimo(C, S, D)
            
            solution, total_cost = metodo_multiplicadores(C, S, D)

            print("\nTabla resuelta por metodo costo minimo")
            C2 = []
            for k in solution:
                C2.append(k.tolist())
            # print(C2)
            print(solution)
            print("Z = ", total_cost)
                        
            matriz, total_cost = costoMinimo(C2, S2, D2)
            print()
            print("La solución óptima por metodo de multiplicadores(MODI) es:")
            for i in matriz:
                print(i)
            print(f"Z = {total_cost}")
            print()
                    
            opc2 = str(input("\nPresiona 1 para volver a comenzar el programa.\nPresiona 2 para salir del programa\nOpcion: "))
            if opc2 == "1":
                os.system("cls")
                pass
            elif "2":
                print("Saliendo del programa")
                break
            else:
                try:
                    while True: 
                        if opc2 != "1" and opc2 != "2":
                            print("Opcion no valida")
                            opc2 = str(input("Introduce de nuevo la opcion: "))
                except:
                    print("No me va a tronar el codigo")
        except:
            print("No me va a tronar el codigo")

if __name__ == "__main__":
    main()