from Funciones_Automatas.automatas import *
from Funciones_Gramaticas.gramaticas import *


# Funcion que crea el menu de automatas y permite navegar en sus opciones:
'''
1.- Cargar automata
2.- Tipo de automata
3.- La cadena es aceptada o no es aceptada
4.-AFND - AFD
5.- Min AFD
6.- Salir
'''
def Automatas():
    try:
        archivo = str(input("Introduce el nombre de el archivo: "))
        archivo = open(archivo, 'r', encoding='utf8')
        lista_automata = archivo.readlines()

        # CantidadEstados = int(lista_automata[0])
        # TamanoSigma = int(lista_automata[1])
        # TamanoF = int(lista_automata[2])
        # sig = LimpiarListaLlavesNTP(lista_automata[3])
        # vector_F = LimpiarListaLlavesNTP(lista_automata[4])
        # Matriz1 = LimpiarListaMatriz(lista_automata)
        # if detectar_AFNDw(Matriz1):
        #     print("Tiene transiciones en vacio")
        #     Matriz1 = MatrizNone(lista_automata)
        # Estado_inicial = sig[0]
        # diccionario_transiciones = Matriz_to_DictTransiciones(Matriz1, sig)
        # estados = estados_get(diccionario_transiciones)
        # p = transformar_diccionario_a_lista(diccionario_transiciones)
        # estados_nfa = obtener_estados_afnd(p)
        # transiciones_dfa, estados_dfa, estados_iniciales_dfa, estados_aceptacion_dfa = to_AFD(p, Estado_inicial, vector_F, sig)
        # simbolos = list(set([simbolo for _, simbolo, _ in p]))
    except:
        print("No va tronar mi codigo:)")

    os.system("cls")
    try:
        while True:
            CantidadEstados = int(lista_automata[0])
            TamanoSigma = int(lista_automata[1])
            TamanoF = int(lista_automata[2])
            sig = LimpiarListaLlavesNTP(lista_automata[3])
            vector_F = LimpiarListaLlavesNTP(lista_automata[4])
            Matriz1 = LimpiarListaMatriz(lista_automata)
            banderaAutomata = TipoAutomata(Matriz1)
            if detectar_AFNDw(Matriz1):
                print("Tiene transiciones en vacio")
                Matriz1 = MatrizNone(lista_automata)
            Estado_inicial = sig[0]
            estados_iniciales_nfa = [0]
            diccionario_transiciones = Matriz_to_DictTransiciones(Matriz1, sig)
            estados = estados_get(diccionario_transiciones)
            p = transformar_diccionario_a_lista(diccionario_transiciones)
            estados_nfa = obtener_estados_afnd(p)
            simbolos = list(set([simbolo for _, simbolo, _ in p]))
            transiciones_dfa, estados_dfa, estados_iniciales_dfa, estados_aceptacion_dfa = to_AFD(p, estados_iniciales_nfa, vector_F, simbolos)
            os.system("cls")
            opc2 = str(input(
                "1.- Cargar automata\n2.- Tipo de automata\n3.- La cadena es aceptada o no es aceptada\n4.-AFND - AFD\n5.- Min AFD\n6.- Salir\nOpcion => "))
            match opc2:
                case "1":
                    try:
                        print(f"Cantidad de estados => {CantidadEstados}")
                        print(f"Tamaño de Sigma => {TamanoSigma}")
                        print(f"Tamaño de F => {TamanoF}")
                        print(f"Sig => {sig}")
                        print(f"Vector F => {vector_F}")
                        ImprimirMatriz(Matriz1)
                        time.sleep(6)
                    except:
                        print("No va a tronar mi codigo:)")
                case "2":
                    try:
                        if banderaAutomata:
                            print("Es determinista")
                        else:
                            print("Es no determinista")
                        time.sleep(6)
                    except:
                        print("No va a tronar mi codigo:)")
                case "3":
                    try:
                        CadEv = str(input("Introduce la cadena a evaluar: "))
                        EvaluarCadena(CadEv, sig, vector_F, Matriz1)
                        time.sleep(6)
                    except:
                        print("No va a tronar mi codigo :)")
                case "4":
                    try:
                        print("Transiciones iniciales")
                        tabla2 = generar_tabla_transiciones(p, estados_nfa, simbolos)
                        # print(tabla2)
                        for fila2 in tabla2:
                            print('\t'.join(fila2))
                        print()
                        print("Transiciones del AFD")

                        tabla = generar_tabla_transiciones(transiciones_dfa, estados_dfa, simbolos)
                        for fila in tabla:
                            print('\t'.join(fila))
                        time.sleep(6)
                        os.system("cls")
                    except:
                        print("No va a tronar mi codigo :)")
                case "5":
                    try:
                        # print(diccionario_transiciones)
                        # m = transformar_matriz(transiciones_dfa)
                        Min_AFD(sig, estados, Estado_inicial,
                                vector_F, diccionario_transiciones)
                        time.sleep(6)
                        os.system("cls")
                    except:
                        print("No va a tronar mi codigo :)")
                case "6":
                    os.system("cls")
                    print("Saliendo del programa...")
                    break
                case _:
                    os.system("cls")
                    print("Opcion invalida")
    except:
        print("\nNo va a tronar mi codigo:)")
