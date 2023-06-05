import random


# FUNCIONES PARA LIMPIAR RENGLONES Y PODER ASIGNARLOS A VARIABLES
def LimpiarLista(lista1, lista2):
    for i in range(len(lista1)):
        if lista1[i] == ',' or lista1[i] == '|':
            pass
        else:
            lista2.append(lista1[i])
    return lista2
def LimpiarListaLlavesNTP(renglon):
    lista = renglon.split("{")
    lista = lista[1].split("}")
    lista = lista[0]
    lista = lista.split(",")
    return lista
def LimpiarRegla(lista_automata):
    # Si son varias reglas en el renglon
    if "|" in lista_automata:
        a = lista_automata.split(" > ")
        a = a[1]
        a = a.split(" | ")
        aux = a[-1].split(" ,\n")
        a.append(aux[0])
        a.pop(-2)
        # lista.append(a)
        if "}" in lista_automata:
            aux2 = a[-1].split(" }")
            a.append(aux2[0])
            a.pop(-2)

    # Si solo es una regla en el renglon
    else:
        a = lista_automata.split(" > ")
        a = a[1]
        a = a.split(" ,\n")
        a = a[0]
        # lista.append(a)
    return a
def LimpiarListaMatriz(lista_automata):
    listaP = []

    for i in range(len(lista_automata)):
        if " > " in lista_automata[i]:
            a = (LimpiarRegla(lista_automata[i]))
            listaP.append(a)

    return listaP

#Funcion para imprimir una matriz de una forma grafica
def ImprimirMatriz(matriz):
    print("Matriz: ")
    for i in range(len(matriz)):
        print(matriz[i])

# Funcion que sirve para calcular el numero de reglas recursivas en una gramatica
def ReglasRecursivas(matriz, renglones_p):
    contador = 0
    lista_RR = []
    for i in range(0, len(matriz)):
        for j in range(len(matriz[i])):
            if renglones_p[i] in matriz[i][j]:
                contador += 1
                lista_RR.append(matriz[i][j])
                # print(matriz[i][j])
    print(f"Total de reglas recursivas: {contador}")
    print(lista_RR)
    return lista_RR

# Sirve para convertir una lista de strings a un solo string
# Ejemplo -> a = ['1','0'] 
# print(ListasStringsAString(a))
# Salida: '10'
def ListasStringsAString(lista):
    palabra = ""
    for i in range(len(lista)):
        palabra += lista[i]
    return palabra

# Funcion que sirve para crear cadenas de forma aleatoria con una gramatica
def CrearCadenaEnFormaAleatoria(matriz, renglones_p, vector_n):
    # x = matriz[0]
    y = random.randint(0, len(matriz[0])-1)
    columna_azar = matriz[0][y]
    print(columna_azar)
    while True:
        for i in range(len(columna_azar)):
            for j in range(len(renglones_p)):
                print(columna_azar)
                if renglones_p[j] in columna_azar[i]:
                    # print(columna_azar)
                    z = random.randint(0, len(matriz[j])-1)
                    columna_azar2 = matriz[j][z]
                    columna_azar = list(columna_azar)
                    columna_azar.pop(i)
                    columna_azar.insert(i, columna_azar2)
                    columna_azar = ListasStringsAString(columna_azar)
                    columna_azar = list(columna_azar)
                    # Sumar los conteos de cada valor de T{}
                    # si la suma es sumar al len(columa_azar)
                    # finalizar programa
                    contador = 0
                    for k in range(len(vector_n)):
                        contador += columna_azar.count(vector_n[k])
                    if contador == len(ListasStringsAString(columna_azar)):
                        columna_azar = ListasStringsAString(columna_azar)
                        print(columna_azar)
                        exit()
                    else:
                        columna_azar = ListasStringsAString(columna_azar)
                    # time.sleep(1)

# Funcion que sirve para evaluar una cadena y saber si es aceptada o no en un automata
def EvaluarCadena(cadena, sig, vector_f, matriz):
    cadenaEstados = "0"
    romperfors = False

    for i in range(len(cadena)):
        if romperfors:
            break
        else:
            car = cadena[i]
            for j in range(len(sig)):
                if romperfors:
                    break
                elif sig[j] != car:
                    print("Cadena no valida")

                    romperfors = True
                    break
                else:
                    pos = j
                    for k in range(len(cadenaEstados)):
                        if romperfors:
                            break
                        cadAux = matriz[int(cadenaEstados[k])][pos]
                        cadenaEstados = cadAux
                        cadAux = ""

                        for l in range(len(cadenaEstados)):
                            if romperfors:
                                break
                            else:
                                for m in range(len(vector_f)):
                                    if cadenaEstados[l] == vector_f[m]:
                                        print("Cadena aceptada")

                                        romperfors = True
                                        break
