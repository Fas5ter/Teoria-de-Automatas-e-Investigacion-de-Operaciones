import numpy as np


# Funcion para calcular el costo
def calcular_costo(costo_matriz, supply, demand):
  total_cost = 0
  for i in range(len(supply)):
    for j in range(len(demand)):
      total_cost += costo_matriz[i][j] * supply[i][j]
  return total_cost

# Funcion para encontrar la celda con el menor valor en la matriz
def encontrar_celda_menor(costo_matriz, supply, demand):
  min_cost = float("inf")
  min_i = -1
  min_j = -1
  for i in range(len(supply)):
    for j in range(len(demand)):
      if supply[i] > 0 and demand[j] > 0:
        if costo_matriz[i][j] < min_cost:
          min_cost = costo_matriz[i][j]
          min_i = i
          min_j = j
  return min_i, min_j

# Funcion que resuelve el problema de transporte por metodo de costo minimo
def costoMinimo(costo_matriz, supply, demand):
  plan = [[0 for j in range(len(demand))] for i in range(len(supply))]
  while sum(supply) > 0 and sum(demand) > 0:
    i, j = encontrar_celda_menor(costo_matriz, supply, demand)
    min_supply = min(supply[i], demand[j])
    plan[i][j] = min_supply
    supply[i] -= min_supply
    demand[j] -= min_supply
  return plan, calcular_costo(costo_matriz, plan, demand)

# Funcion para hacer una barra de progreso
def progress_bar(part, total, length=30):
    frac =part / total
    completed = int(frac * length)
    missing = length - completed
    bar = f"[{'#'*completed} {'-'*missing}]{frac:.2%}"
    return bar

# Funcion para validar que cada entrada sea de tipo entero
def validar_entrada_tipo_int(str):
    while True:
        try:
            n = int(input(f'{str}'))
            return n
        except:
            print("Escribir un numero")

# Funcion que sirve para asignar a una variable cada valor de los valores
def RegistrarValores(origenes, destinos):
    # valores = [[0 for x in range(origenes)] for y in range(destinos)]
    valores = np.zeros((origenes, destinos))
    for x in range(origenes):
        for y in range(destinos):
            valores[x][y] = validar_entrada_tipo_int(f'Introducir el valor del origen {x+1} con el destino {y+1}\n')
    # print(valores)
    # print(valores.tolist())
    return valores.tolist()

# Funcion que sirve para asignar a una variable el vcada valor de oferta
def RegistrarOfertas(num):
    oferta = []
    for x in range(num):
        aux = validar_entrada_tipo_int(f'Introducir la oferta del origen {x+1}\n')
        oferta.append(aux)
    return oferta

# Funcion que sirve para asignar a una variable el valor de cada demanda
def RegistrarDemandas(num):
    demanda = []
    for x in range(num):
        aux = validar_entrada_tipo_int(f'Introducir la demanda del destino {x+1}\n')
        demanda.append(aux)
    return demanda

# Funcion para asignar a una variable la cantidad de destinos
def Registrar_Val_Destinos():
    while True:
        aux = validar_entrada_tipo_int("Introducir el numero de destinos\n")
        if (aux > 1):
            break
        print('escribir un numero igual o mayor a dos')
    return aux

# Funcion para asignar a una variable la cantidad de origenes
def Registrar_Val_Origenes():
    while True:
        aux = validar_entrada_tipo_int("Introducir el numero de origenes\n")
        if (aux > 1):
            break
        print('escribir un numero igual o mayor a dos')
    return aux

# Funcion que sirve que resuelve el problema de transporte a partir de una solucion inicial dada por costo minimo, por metodo de multiplicadores
def metodo_multiplicadores(costs, supply, demand):
    """
    Encuentra la solución óptima para un problema de transporte usando el método de multiplicadores.

    Args:
        costs (list): Matriz de costos del problema de transporte.
        supply (list): Lista de la oferta de cada fuente.
        demand (list): Lista de la demanda de cada destino.

    Returns:
        Una matriz que indica la cantidad transportada desde cada fuente a cada destino.
    """

    # Crear matriz de costos con ceros adicionales para satisfacer restricciones de demanda y oferta
    rows, cols = len(supply), len(demand)
    cost_matrix = np.zeros((rows, cols))
    cost_matrix[:rows, :cols] = costs
    
    # Inicializar variables auxiliares
    basic_variables = []
    non_basic_variables = []
    u_values = []
    v_values = []
    reduced_costs = np.zeros((rows, cols))

    # Inicializar variables básicas y no básicas
    for i in range(rows):
        for j in range(cols):
            if supply[i] != 0 and demand[j] != 0:
                basic_variables.append((i, j))
            else:
                non_basic_variables.append((i, j))

    # Inicializar valores de u y v en cero
    u_values = [0 for _ in range(rows)]
    v_values = [0 for _ in range(cols)]
    
    # Calcular valores de u y v
    for i, j in basic_variables:
        if u_values[i] == 0 and v_values[j] == 0:
            u_values[i] = cost_matrix[i][j]
        elif u_values[i] != 0 and v_values[j] == 0:
            v_values[j] = cost_matrix[i][j] - u_values[i]
        elif u_values[i] == 0 and v_values[j] != 0:
            u_values[i] = cost_matrix[i][j] - v_values[j]

    # Iterar hasta encontrar una solución óptima
    while True:
        # Actualizar valores reducidos
        for i, j in non_basic_variables:
            reduced_costs[i][j] = cost_matrix[i][j] - u_values[i] - v_values[j]

        # Encontrar celda con el menor costo reducido
        i_min, j_min = np.unravel_index(reduced_costs.argmin(), reduced_costs.shape)
        min_reduced_cost = reduced_costs[i_min][j_min]

        # Verificar si se encontró una ruta de mejora válida
        if min_reduced_cost >= 0:
            # No se encontró una ruta de mejora válida, la solución es óptima
            solution = np.zeros((rows, cols))
            for i, j in basic_variables:
                solution[i][j] = supply[i] if supply[i] <= demand[j] else demand[j]
                supply[i] -= solution[i][j]
                demand[j] -= solution[i][j]
            total_cost = np.sum(solution * cost_matrix)
            return solution, total_cost

        # Calcular el ciclo que incluye la celda de menor costo reducido
        cycle = [(i_min, j_min)]
        visited_rows = set()
        visited_cols = set()
        visited_rows.add(i_min)
        visited_cols.add(j_min)
        while True:
            # Buscar en la fila del último elemento del ciclo
            for j in range(cols):
                if (cycle[-1][0], j) in basic_variables and j not in visited_cols:
                    cycle.append((cycle[-1][0], j))
                    visited_cols.add(j)
                    break
            else:
                # Buscar en la columna del último elemento del ciclo
                for i in range(rows):
                    if (i, cycle[-1][1]) in basic_variables and i not in visited_rows:
                        cycle.append((i, cycle[-1][1]))
                        visited_rows.add(i)
                        break
                else:
                    # No se encontró un ciclo, error en los datos
                    raise Exception("Error en los datos")

            # Verificar si se ha cerrado el ciclo
            if cycle[0][0] == cycle[-1][0] or cycle[0][1] == cycle[-1][1]:
                break

        # Calcular delta y actualizar valores de u y v
        delta = min(supply[cycle[i][0]] - demand[cycle[i][1]] for i in range(1, len(cycle), 2))
        for i, j in basic_variables:
            if (i, j) in cycle[1::2]:
                supply[i] -= delta
                demand[j] += delta
            elif (i, j) in cycle[0::2]:
                supply[i] += delta
                demand[j] -= delta
        for i in range(rows):
            if i in visited_rows:
                u_values[i] += delta
        for j in range(cols):
            if j in visited_cols:
                v_values[j] -= delta
        # Actualizar valores reducidos
        for i, j in non_basic_variables:
            reduced_costs[i][j] = cost_matrix[i][j] - u_values[i] - v_values[j]

        # Encontrar celda con el menor costo reducido
        i_min, j_min = np.unravel_index(reduced_costs.argmin(), reduced_costs.shape)
        min_reduced_cost = reduced_costs[i_min][j_min]

        # Verificar si se encontró una ruta de mejora válida
        if min_reduced_cost >= 0:
            # No se encontró una ruta de mejora válida, la solución es óptima
            solution = np.zeros((rows, cols))
            for i, j in basic_variables:
                solution[i][j] = supply[i] if supply[i] <= demand[j] else demand[j]
                supply[i] -= solution[i][j]
                demand[j] -= solution[i][j]
            total_cost = np.sum(solution * cost_matrix)
            return solution, total_cost

# Funcion para pasar una matriz en formato np.array a una matriz normal tipo list
def numpy_to_list(matriz):
    """
    Convierte una matriz de numpy a una matriz normal (lista de listas).
    
    Args:
        matrix (numpy.ndarray): La matriz de numpy a convertir.
    
    Returns:
        list: La matriz normal resultante.
    """
    return matriz.tolist()

def crear_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            elemento = int(input("Ingrese un elemento: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz
