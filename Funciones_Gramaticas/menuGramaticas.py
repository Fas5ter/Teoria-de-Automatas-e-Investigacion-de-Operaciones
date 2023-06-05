from Funciones_Gramaticas.gramaticas import *


# Funcion que crea el menu de gramaticas y permite navegar en sus opciones:
'''
1.- Cargar Gramatica en Memoria.
2.- Generar Cadenas Aleatorias.
3.- Generar el total de reglas de recursividad y el total de reglas recursivas
4.- Salir.
'''
def Gramaticas():
    try:
        # GRAMATICA 1
        archivo = open('Gram1.txt', 'r', encoding='utf8')
        lista_automata = archivo.readlines()
        tamano_n = int(lista_automata[0])
        tamano_t = int(lista_automata[2])
        tamano_p = int(lista_automata[3])
        renglones_p = LimpiarListaLlavesNTP(lista_automata[4])
        vector_n = LimpiarListaLlavesNTP(lista_automata[5])
        # GRAMATICA 2
        archivo2 = open('Gram2.txt', 'r', encoding='utf8')
        lista_automata2 = archivo2.readlines()
        tamano_n2 = int(lista_automata2[0])
        tamano_t2 = int(lista_automata2[2])
        tamano_p2 = int(lista_automata2[3])
        renglones_p2 = LimpiarListaLlavesNTP(lista_automata2[4])
        vector_n2 = LimpiarListaLlavesNTP(lista_automata2[5])
        # GRAMATICA 3
        archivo3 = open('Gram3.txt', 'r', encoding='utf8')
        lista_automata3 = archivo3.readlines()
        tamano_n3 = int(lista_automata3[0])
        tamano_t3 = int(lista_automata3[2])
        tamano_p3 = int(lista_automata3[3])
        renglones_p3 = LimpiarListaLlavesNTP(lista_automata3[4])
        vector_n3 = LimpiarListaLlavesNTP(lista_automata3[5])

        Matriz1 = LimpiarListaMatriz(lista_automata)
        Matriz2 = LimpiarListaMatriz(lista_automata2)
        Matriz3 = LimpiarListaMatriz(lista_automata3)
    except Exception as e:
        print("Dato no valido")
    finally:

        while True:
            os.system("cls")
            print("########### PROGRAMA QUE CARGA GRAMATICAS, GENERA CADENAS ALEATORIAS Y ENCUENTRA REGLAS DE RECURSIVIDAD ##########")
            print("1.- Cargar Gramatica en Memoria.")
            print("2.- Generar Cadenas Aleatorias.")
            print(
                "3.- Generar el total de reglas de recursividad y el total de reglas recursivas")
            print("4.- Salir.")
            opc = str(input("Opcion: "))
            print("")
            match opc:
                case "1":
                    os.system("cls")
                    print("GRAMATICA 1")
                    print(f"Tamaño de N = {tamano_n}")
                    print(f"Tamaño de T = {tamano_t}")
                    print(f"Tamaño de P = {tamano_p}")
                    print(f"Renglones de P: {renglones_p}")
                    print(f"Vector N: {vector_n}")
                    ImprimirMatriz(Matriz1)
                    print("###############################")
                    print("GRAMATICA 2")
                    print(f"Tamaño de N = {tamano_n2}")
                    print(f"Tamaño de T = {tamano_t2}")
                    print(f"Tamaño de P = {tamano_p2}")
                    print(f"Renglones de P: {renglones_p2}")
                    print(f"Vector N: {vector_n2}")
                    ImprimirMatriz(Matriz2)
                    print("###############################")
                    print("GRAMATICA 3")
                    print(f"Tamaño de N = {tamano_n3}")
                    print(f"Tamaño de T = {tamano_t3}")
                    print(f"Tamaño de P = {tamano_p3}")
                    print(f"Renglones de P: {renglones_p3}")
                    print(f"Vector N: {vector_n3}")
                    ImprimirMatriz(Matriz3)
                    opc2 = str(
                        input("Digite 1 para regresar al menú o 2 para salir del programa: "))
                    if opc2 == '2':
                        print("Saliendo del programa...")
                        return True
                    else:
                        pass

                case '2':
                    os.system("cls")
                    opc = str(input(
                        "Ingrese con que matriz generar una cadena en forma aleatoria.\nA) Matriz 1\nB) Matriz 2\nC) Matriz 3\nOpcion: ").upper())
                    match opc:
                        case 'A':
                            CrearCadenaEnFormaAleatoria(
                                Matriz1, renglones_p, vector_n)
                        case 'B':
                            CrearCadenaEnFormaAleatoria(
                                Matriz2, renglones_p2, vector_n2)
                        case 'C':
                            CrearCadenaEnFormaAleatoria(
                                Matriz3, renglones_p3, vector_n3)
                        case default: break

                case '3':
                    os.system("cls")
                    print("Reglas recursivas matriz 1:")
                    ReglasRecursivas(Matriz1, renglones_p)
                    print("Reglas recursivas matriz 2:")
                    ReglasRecursivas(Matriz2, renglones_p2)
                    print("Reglas recursivas matriz 3:")
                    ReglasRecursivas(Matriz3, renglones_p3)
                    opc2 = str(
                        input("Digite 1 para regresar al menú o 2 para salir del programa: "))
                    if opc2 == '2':
                        print("Saliendo del programa...")
                        break
                    else:
                        pass

                case '4':
                    os.system("cls")
                    print("Saliendo del programa...")
                    break
