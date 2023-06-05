import os
import random
import time
from Funciones_Gramaticas.gramaticas import *


def MatrizNone(lista_automata):
    listaP = []

    for i in range(len(lista_automata)):
        if " > " in lista_automata[i]:
            a = (LimpiarRegla(lista_automata[i]))
            listaP.append(a)
            
    for i in range(len(listaP)):
        for j in range(len(listaP[i])):
            if listaP[i][j] == "NULL":
                listaP[i][j] = None

    return listaP


# Para detectar si hay transiciones en vacio
def detectar_AFNDw(Matriz1):
    a = False
    for i in (Matriz1):
        if a:
            break
        for j in i:
            if "NULL" in j:
                # print("Tiene transiciones en vacio")
                a = True
                break
    return a

# Funcion que se introduce una matriz y te retorna que tipo de automata es
def TipoAutomata(Matriz):
    try:
        banderaDeterminista = True
        for k in range(len(Matriz)):
            for l in range(len(Matriz[k])):
                if len(Matriz[k][l]) > 1:
                    banderaDeterminista = False

        if banderaDeterminista:
            print("Automata determinista")

        else:
            print("Automata no determinista")
    except:
        print("No va a tronar mi codigo:)")

# Funcion que se introduce una matriz y te retorna True si es definido, si es no definido retorna False
def TipoAutomata2(Matriz):
    try:
        banderaDeterminista = True
        for k in range(len(Matriz)):
            for l in range(len(Matriz[k])):
                if len(Matriz[k][l]) > 1:
                    banderaDeterminista = False

        """ if banderaDeterminista:
            print("Automata determinista")
            
        else:
            print("Automata no determinista") """
        return banderaDeterminista
    except:
        print("No va a tronar mi codigo:)")

""" La función cerradura es una función que implementa el algoritmo de cierre transitivo epsilon en un autómata finito no determinista (NFA).
El algoritmo de cierre transitivo epsilon se utiliza para encontrar todos los estados a los que se puede llegar desde un estado dado en un NFA sin consumir ninguna entrada. 
Para esto, se sigue la transición epsilon desde el estado dado y se visita cada estado al que se llega a través de una transición epsilon. Luego, se busca en cada uno de 
estos estados las transiciones que se pueden seguir sin consumir ninguna entrada y se visitan los estados a los que se llega a través de estas transiciones. 
Este proceso se repite hasta que ya no se pueden visitar más estados.
La función cerradura toma como entrada un estado en un NFA y la lista de transiciones del NFA. Primero, se agrega el estado de entrada a un conjunto c. 
Luego, se buscan todas las transiciones que salen del estado de entrada y que no consumen ninguna entrada (es decir, las transiciones epsilon). 
Para cada una de estas transiciones, se agrega el estado al que se llega a través de la transición a c. 
Luego, se busca si hay transiciones epsilon que salen de los estados agregados recientemente y se agregan los estados alcanzables a c. 
Este proceso se repite hasta que no se pueden agregar más estados. 
Finalmente, la función devuelve el conjunto c, que contiene todos los estados a los que se puede llegar desde el estado de entrada sin consumir ninguna entrada. """
# def cerradura(estado, transiciones):
#     c = set([estado]) if isinstance(estado, int) else set([tuple(estado)])
#     for e in c:
#         for transicion in transiciones:
#             if e == transicion[0] and transicion[1] == 'NULL':
#                 t = transicion[2]
#                 if isinstance(t, int):
#                     c.add(t)
#                 else:
#                     for i in t:
#                         c.add(i)
#     return sorted(list(c))

""" La función mover(estado, simbolo, transiciones) toma como entrada un estado, un símbolo y un conjunto de transiciones de un autómata, y devuelve un conjunto de estados
que puede alcanzar el autómata desde el estado actual al leer el símbolo dado.
La función comienza creando un conjunto vacío mover_estado, que contendrá los estados alcanzables desde estado al leer simbolo.
Luego, se itera sobre las transiciones del autómata, y si se encuentra una transición que tiene como estado de origen el estado actual y el símbolo leído
es igual al símbolo de entrada, se agrega el estado de destino de esa transición al conjunto mover_estado.
Finalmente, la función devuelve el conjunto mover_estado que contiene todos los estados que se pueden alcanzar desde estado al leer simbolo. """
# def mover(estado, simbolo, transiciones):
#     mover_estado = set()
#     for transicion in transiciones:
#         if transicion[0] in estado and transicion[1] == simbolo:
#             mover_estado.add(tuple(transicion[2]))
#     return mover_estado

""" Definir la función que convierte el AFN al AFD
La función to_AFD recibe como entrada los siguientes parámetros:
transiciones_nfa: lista de transiciones del NFA. Cada transición se representa por una lista de tres elementos: estado origen, símbolo de transición y conjunto de estados destino.
estados_iniciales_nfa: lista con el estado inicial del NFA.
estados_aceptacion_nfa: lista de estados de aceptación del NFA.
simbolos: lista de símbolos del alfabeto del NFA.
La función tiene como objetivo construir un AFD equivalente al NFA de entrada. La idea general de la función es utilizar el algoritmo de construcción de subconjuntos,
que consiste en crear estados del AFD a partir de conjuntos de estados del NFA.
En primer lugar, se inicializan las listas estados_dfa, transiciones_dfa, estados_iniciales_dfa y estados_aceptacion_dfa. La lista estados_dfa contiene los estados del AFD, 
que son conjuntos de estados del NFA. La lista transiciones_dfa contiene las transiciones del AFD, que se construyen a partir de las transiciones del NFA. 
Las listas estados_iniciales_dfa y estados_aceptacion_dfa contienen el estado inicial y los estados de aceptación del AFD, respectivamente.
El primer paso es crear el estado inicial del AFD a partir del cierre-épsilon del estado inicial del NFA. Se agrega este estado inicial a las 
listas estados_dfa y estados_iniciales_dfa.
Luego, se inicia un ciclo while que itera sobre los estados del AFD que aún no han sido procesados.
Para cada estado del AFD, se itera sobre los símbolos del alfabeto y se construye el conjunto de estados del NFA a los que se llega desde el estado actual del 
AFD mediante una transición con el símbolo en cuestión. Este conjunto se obtiene aplicando la función mover al estado actual y al símbolo. 
Luego, se calcula el cierre-épsilon de este conjunto utilizando la función cerradura. Si el conjunto resultante no se encuentra en la lista de estados del AFD y no es vacío, 
se agrega a la lista estados_dfa.
Después, se agrega a la lista transiciones_dfa la transición del AFD correspondiente al estado actual del AFD, el símbolo en cuestión y el estado obtenido a partir del 
conjunto de estados del NFA.
Finalmente, se busca en los conjuntos de estados del AFD aquellos que contienen al menos un estado de aceptación del NFA. 
Estos conjuntos se agregan a la lista estados_aceptacion_dfa. 
La función devuelve las listas transiciones_dfa, estados_dfa, estados_iniciales_dfa y estados_aceptacion_dfa, que representan el AFD construido a partir del NFA de entrada. """
# def to_AFD(transiciones_nfa, estados_iniciales_nfa, estados_aceptacion_nfa, simbolos):
#     estados_dfa = []
#     transiciones_dfa = []
#     estados_iniciales_dfa = []
#     estados_aceptacion_dfa = []

#     estado_inicial = cerradura(estados_iniciales_nfa[0], transiciones_nfa)
#     estados_dfa.append(estado_inicial)
#     estados_iniciales_dfa.append(estado_inicial)
#     i = 0
#     while i < len(estados_dfa):
#         for s in simbolos:
#             t = cerradura(
#                 mover(estados_dfa[i], s, transiciones_nfa), transiciones_nfa)
#             if t not in estados_dfa and t != []:
#                 estados_dfa.append(t)
#             transiciones_dfa.append([i, s, estados_dfa.index(t)])
#         i += 1
#     for e in estados_dfa:
#         for j in e:
#             if j in estados_aceptacion_nfa:
#                 estados_aceptacion_dfa.append(estados_dfa.index(e))
#                 break
#     return transiciones_dfa, estados_dfa, estados_iniciales_dfa, estados_aceptacion_dfa

# def to_AFD(transiciones_nfa, estados_iniciales_nfa, estados_aceptacion_nfa, simbolos):
#     estados_dfa = []
#     transiciones_dfa = []
#     estados_iniciales_dfa = []
#     estados_aceptacion_dfa = []

#     estado_inicial = cerradura(estados_iniciales_nfa[0], transiciones_nfa)
#     estados_dfa.append(estado_inicial)
#     estados_iniciales_dfa.append(estado_inicial)
#     i = 0
#     while i < len(estados_dfa):
#         for s in simbolos:
#             t = cerradura(
#                 mover(estados_dfa[i], s, transiciones_nfa), transiciones_nfa)
#             if t not in estados_dfa and t != []:
#                 estados_dfa.append(t)
#             transiciones_dfa.append([i, s, estados_dfa.index(t)])
#         i += 1
#     for e in estados_dfa:
#         for j in e:
#             if j in estados_aceptacion_nfa:
#                 estados_aceptacion_dfa.append(estados_dfa.index(e))
#                 break
#     return transiciones_dfa, estados_dfa, estados_iniciales_dfa, estados_aceptacion_dfa

# Funcion que imprime los resultados de convertir el AFND a un AFD
def imprimirResultadosAFND_AFD(Matriz1, sig, vector_F):
    if TipoAutomata2(Matriz1):
        print("Es determinista")
    else:
        print("No es determinista")
        transiciones_nfa = []
        estados_iniciales_nfa = [int(sig[0])]
        estados_aceptacion_nfa = []
        for x in range(len(vector_F)):
            estados_aceptacion_nfa.append(int(vector_F[x]))
        # transiciones de la tabla de transiciones
        for i in range(len(Matriz1)):
            for j in range(len(Matriz1[i])):
                auxg = set()
                for k in range(len(Matriz1[i][j])):
                    if len(Matriz1[i][j]) > 1:
                        for l in range(len(Matriz1[i][j])):
                            p = list(Matriz1[i][j])
                            for m in range(len(p)):
                                auxg.add(p[m])
                    else:
                        auxg.add(Matriz1[i][j])
                    if len(auxg) == len(Matriz1[i][j]):
                        break
                transiciones_nfa.append([int(i), str(j), auxg])

        # estados_iniciales_nfa = [0]
        # estados_aceptacion_nfa = [0, 3]
        simbolos = sig

        transiciones_dfa, estados_dfa, estados_iniciales_dfa, estados_aceptacion_dfa = to_AFD(
            transiciones_nfa, estados_iniciales_nfa, estados_aceptacion_nfa, simbolos)

        # transiciones_dfa: Esta variable almacena las transiciones del AFD resultante
        # en forma de lista de tuplas. Cada tupla tiene tres elementos:
        # el primer elemento es el estado de partida de la transición,
        # el segundo elemento es el símbolo que se utiliza en la transición y
        # el tercer elemento es el estado de llegada de la transición.
        # En este caso, la salida muestra las transiciones del AFD resultante.
        print("Transiciones AFD:")
        for t in transiciones_dfa:
            print(t)
        # estados_dfa: Esta variable almacena los estados del AFD resultante en
        # forma de conjunto. En este caso, la salida muestra los estados del AFD
        # resultante.
        print("Estados AFD:")
        for e in estados_dfa:
            print(e)
        # # estados_iniciales_dfa: Esta variable almacena el estado inicial del AFD
        # resultante. En este caso, la salida muestra el estado inicial del
        # AFD resultante.
        print("Estado inicial AFD:")
        print(estados_iniciales_dfa)
        # # estados_aceptacion_dfa: Esta variable almacena los estados de aceptación
        # del AFD resultante en forma de conjunto.
        # En este caso, la salida muestra los estados de aceptación del AFD resultante.
        print("Estados de aceptación AFD:")
        print(estados_aceptacion_dfa)

# Funcion que sirve para convertir una matriz de estados de un AF(N)D a un diccionario de transiciones
def Matriz_to_DictTransiciones(matriz, Sigma):
    tabla_transiciones = {}
    for i in range(len(matriz)):
        estado = str(i)
        transiciones = {}
        for j in range(len(Sigma)):
            simbolo = Sigma[j]
            estado_destino = matriz[i][j]
            transiciones[simbolo] = estado_destino
        tabla_transiciones[estado] = transiciones
    return tabla_transiciones

def transformar_matriz(matriz):
    resultado = {}
    for fila in matriz:
        estado_actual = str(fila[0])
        entrada = str(fila[1])
        estado_siguiente = str(fila[2])
        
        if estado_actual not in resultado:
            resultado[estado_actual] = {}
        
        resultado[estado_actual][entrada] = estado_siguiente
    
    return resultado


# Funcion que sirve para minimizar un AFD
def Min_AFD(Sigma, Estados, Estado_inicial, Estados_finales, Transiciones):
    '''
    ALGORITMO PARA MINIMIZAR UN AFD
    1.- Particionamiento inicial: En este paso, se divide el conjunto de estados del autómata en dos conjuntos, uno que contiene los estados
    finales y otro que contiene los estados no finales.

    2.- Particionamiento de los estados: En este paso, se divide cada conjunto resultante de la partición anterior en subconjuntos más pequeños
    de acuerdo con las transiciones que salen de los estados en cada subconjunto. Los estados que tienen transiciones que van a diferentes subconjuntos
    deben colocarse en conjuntos diferentes.

    3.- Repetición del segundo paso: Este paso se repite hasta que no se pueden realizar más divisiones en ninguno de los conjuntos. 
    En este punto, se obtiene la partición final de los estados, y cada conjunto representa un estado en el autómata minimizado.
    '''
    # Paso 1: Inicialización
    n = len(Estados)
    particion_actual = [set(Estados_finales), set(
        Estados) - set(Estados_finales)]
    particion_anterior = []

    # Paso 2: División
    while particion_actual != particion_anterior:
        particion_anterior = particion_actual.copy()
        for i, particion in enumerate(particion_actual):
            for simbolo in Sigma:
                transiciones = {}
                for estado in particion:
                    if Transiciones[estado].get(simbolo) is None:
                        estado_destino = None
                    else:
                        estado_destino = Transiciones[estado][simbolo]
                    if estado_destino in transiciones:
                        transiciones[estado_destino].add(estado)
                    else:
                        transiciones[estado_destino] = {estado}
                particion_actual[i] = set.union(particion_actual[i], *[particion_actual[j] for j in range(len(particion_actual)) if transiciones.get(
                    list(particion_actual[j])[0]) is not None and len(particion_actual[j] & transiciones[list(particion_actual[j])[0]]) > 0])
                particion_actual.extend([particion_actual[j] & transiciones[list(particion_actual[j])[0]] for j in range(len(particion_actual)) if transiciones.get(list(
                    particion_actual[j])[0]) is not None and len(particion_actual[j] & transiciones[list(particion_actual[j])[0]]) > 0 and particion_actual[j] not in particion_actual])

    # Paso 3: Crear la tabla de transiciones minimizada
    tabla_transiciones_minimizada = {}
    for particion in particion_actual:
        estado = list(particion)[0]
        tabla_transiciones_minimizada[estado] = {}
        for simbolo in Sigma:
            estado_destino = None
            for estado_en_particion in particion:
                if Transiciones[estado_en_particion].get(simbolo) is not None:
                    estado_destino = Transiciones[estado_en_particion][simbolo]
                    break
            for particion_destino in particion_actual:
                if estado_destino in particion_destino:
                    tabla_transiciones_minimizada[estado][simbolo] = list(particion_destino)[
                        0]
                    break

    # Paso 4: Imprimir la tabla de transiciones minimizada
    print("La nueva tabla de transiciones ya minimizada:")
    for estado, transiciones in tabla_transiciones_minimizada.items():
        for simbolo, estado_destino in transiciones.items():
            print(f"{estado} > {simbolo} | {estado_destino}")

    # Paso 5: Crear el autómata minimizado
    estados_minimizados = list(particion_actual)
    estados_finales_minimizados = [
        particion for particion in particion_actual if particion & set(Estados_finales)]
    estado_inicial_minimizado = [
        particion for particion in particion_actual if Estado_inicial in particion][0]

    # print("Los estados minimizados:", estados_minimizados)
    # print("Los nuevos estados finales serán los que contengan al menos un estado final de los estados finales antes de minimizarlo.")
    # print("Los estados finales minimizados:", estados_finales_minimizados)
    # print("El estado inicial minimizado:", estado_inicial_minimizado)

    # Imprimir el autómata minimizado
    print("\nAutómata minimizado:")
    for i, estado_minimizado in enumerate(estados_minimizados):
        print(f"{i} : {estado_minimizado}")
        if estado_minimizado in estados_finales_minimizados:
            print(f"{i} es un estado final")
        if estado_minimizado == estado_inicial_minimizado:
            print(f"{i} es el estado inicial")
        for simbolo in Sigma:
            estado_destino_minimizado = tabla_transiciones_minimizada[list(estado_minimizado)[
                0]].get(simbolo)
            for j, estado_minimizado_destino in enumerate(estados_minimizados):
                if estado_destino_minimizado in estado_minimizado_destino:
                    print(f"{i} --{simbolo}--> {j}")
                    break

# Funcion que sirve para obtener los estados un diccionario de transiciones
def estados_get(transicionesDict):
    estados = []
    for estado in transicionesDict:
        estados.append(estado)
    return estados


def cerradura(estado, transiciones):
    c = set()  # Conjunto vacío
    pila = []
    if isinstance(estado, int):
        pila.append(estado)
    else:
        pila.extend(estado)
    while pila:
        e = pila.pop()
        c.add(e)
        for transicion in transiciones:
            if e == transicion[0] and transicion[1] == '@':
                t = transicion[2]
                if isinstance(t, int):
                    pila.append(t)
                else:
                    pila.extend(t)
    return sorted(list(c))

def mover(estado, simbolo, transiciones):
    mover_estado = set()
    for transicion in transiciones:
        if transicion[0] in estado and transicion[1] == simbolo:
            t = transicion[2]
            if isinstance(t, int):
                mover_estado.add(t)
            else:
                mover_estado.update(t)
    return mover_estado

def to_AFD(transiciones_nfa, estados_iniciales_nfa, estados_aceptacion_nfa, simbolos):
    estados_dfa = []
    transiciones_dfa = []
    estados_iniciales_dfa = []
    estados_aceptacion_dfa = []

    estado_inicial = cerradura(estados_iniciales_nfa[0], transiciones_nfa)
    estados_dfa.append(estado_inicial)
    estados_iniciales_dfa.append(estado_inicial)
    i = 0
    while i < len(estados_dfa):
        for s in simbolos:
            t = cerradura(
                mover(estados_dfa[i], s, transiciones_nfa), transiciones_nfa)
            if t not in estados_dfa and t != []:
                estados_dfa.append(t)
            if t != []:
                transiciones_dfa.append([i, s, estados_dfa.index(t)])
        i += 1
    for e in estados_dfa:
        for j in e:
            if j in estados_aceptacion_nfa:
                estados_aceptacion_dfa.append(estados_dfa.index(e))
                break
    return transiciones_dfa, estados_dfa, estados_iniciales_dfa, estados_aceptacion_dfa

def generar_tabla_transiciones(transiciones_dfa, estados_dfa, simbolos):
    tabla_transiciones = []

    # Encabezado de la tabla
    encabezado = ['Estados'] + simbolos
    tabla_transiciones.append(encabezado)

    # Filas de la tabla
    for i, estado in enumerate(estados_dfa):
        fila = [f'q{i}']  # Estado actual
        for simbolo in simbolos:
            siguiente_estado = obtener_siguiente_estado(i, simbolo, transiciones_dfa)
            if siguiente_estado == -1:
                fila.append(f'-')
            else:
                fila.append(f'q{siguiente_estado}')
        tabla_transiciones.append(fila)
    return tabla_transiciones

def obtener_siguiente_estado(estado_actual, simbolo, transiciones_dfa):
    for transicion in transiciones_dfa:
        if transicion[0] == estado_actual and transicion[1] == simbolo:
            return transicion[2]
    return -1

def obtener_estados_afnd(transiciones_nfa):
    estados = set()

    for transicion in transiciones_nfa:
        estado_origen = transicion[0]
        estado_destino = transicion[2]

        estados.add(estado_origen)
        if isinstance(estado_destino, list):
            estados.update(estado_destino)
        else:
            estados.add(estado_destino)

    return list(estados)

def transformar_diccionario_a_lista(diccionario):
    lista = []
    for estado, transiciones in diccionario.items():
        for simbolo, siguiente_estado in transiciones.items():
            estado_actual = int(estado)
            simbolo_actual = simbolo
            if siguiente_estado == None :
                siguiente_estado = []
            else:
                siguiente_estado = [int(e) for e in siguiente_estado]
            lista.append([estado_actual, simbolo_actual, siguiente_estado])
    return lista
