# Algoritmo SIN tabla auxiliar:

# Entrada:
# n: cantidad total de tareas
# restricciones: lista de tuplas que representan las restricciones entre tareas

# Precondición:
# n es un entero positivo mayor que cero
# restricciones es una lista de tuplas donde cada tupla contiene dos enteros que representan las tareas y sus restricciones

# Procedimiento de cálculo:



'''
Inicialización: Se preparan estructuras para almacenar predecesores y grados de entrada de las tareas.
Construcción de relaciones: Se determinan las tareas previas para cada tarea y se calcula cuántas tareas deben completarse antes de comenzar cada tarea.
Inicio: Se agregan a una cola las tareas que no tienen tareas previas.
Recorrido de la cola: Se procesan las tareas en orden de su grado de entrada. Se van eliminando de la cola y se agregan al orden topológico. Luego, se actualiza el grado de entrada de las tareas siguientes.
Verificación de ciclos: Se confirma si todas las tareas se incluyeron en el orden topológico. Si no, significa que hay un ciclo y se informa.
'''    
# Fin de ordenacion_topologica

# Poscondición:
# Si no hay ciclos, retorna una lista con el orden topológico de las tareas. Si hay ciclos, retorna un mensaje indicando que no es posible ordenar las tareas.

# Salida:
# Una lista con el orden topológico de las tareas o un mensaje indicando que no es posible ordenar las tareas debido a ciclos.



def ordenacion_topologica(n, restricciones):
    predecesores = {} # Diccionario para almacenar los predecesores de cada tarea
    grado_entrada = {} # Diccionario para almacenar el grado de entrada de cada tarea
    orden_topologico = [] # Lista para almacenar el orden topológico de las tareas

    # Construimos la lista de predecesores y calculamos el grado de entrada de cada tarea
    for i in range(1, n + 1):
        predecesores[i] = []
        grado_entrada[i] = 0

    for i, j in restricciones:
        predecesores[j].append(i) # Invertimos el orden para calcular el grado de entrada
        grado_entrada[i] += 1

    # Inicializamos una cola para almacenar las tareas sin predecesores
    cola = []

    # Añadimos las tareas sin predecesores a la cola
    for tarea, grado in grado_entrada.items():
        if grado == 0:
            cola.append(tarea)

    
    while cola:
        # Sacamos una tarea de la cola
        tarea_actual = cola.pop(0)
        orden_topologico.append(tarea_actual)

        
        for sucesor in predecesores[tarea_actual]:
            # Decrementamos en 1 el grado de entrada del sucesor
            grado_entrada[sucesor] -= 1

            
            if grado_entrada[sucesor] == 0:
                # Si el sucesor no tiene más predecesores añadimos el sucesor a la cola
                cola.append(sucesor)

    # Si el orden topológico tiene todas las tareas
    if len(orden_topologico) == n:
        return orden_topologico
    else:
        return "No es posible ordenar las tareas debido a ciclos"

# Ejemplo de uso
n = 5
restricciones = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
resultado = ordenacion_topologica(n, restricciones)
print("Orden topológico de las tareas:", resultado)
