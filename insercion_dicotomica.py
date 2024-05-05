# Algoritmo SIN tabla auxiliar:

# Entrada:
# t: TABLA[ENTEROS][1,n] a ser ordenada

# Precondición:
# t es una lista de enteros que puede estar desordenada

# Procedimiento de cálculo:

'''
Inicialización: Se crea una lista vacía para almacenar la tabla ordenada.
Iteración: Se recorre cada elemento de la tabla original.
Búsqueda binaria: Para cada elemento, se encuentra su posición de inserción en la lista ordenada 
utilizando búsqueda binaria. Divide repetidamente el espacio de búsqueda a la mitad, comparando el 
elemento buscado con el elemento en el medio de la lista. 
Inserción: El elemento se inserta en la posición encontrada en la lista ordenada.
Retorno: Se devuelve la lista ordenada.
'''

# Fin de binary_insertion_sort

# Poscondición:
# La tabla t ha sido ordenada de manera ascendente utilizando el algoritmo de ordenación por inserción binaria.

# Salida:
# Una lista con los elementos de t ordenados de manera ascendente.



def binary_insertion_sort(t):
    r = []
    for element in t:
        low, high = 0, len(r) - 1
        while low <= high:
            mid = (low + high) // 2
            if element < r[mid]:
                high = mid - 1
            elif element > r[mid]:
                low = mid + 1
            else:
                break
        if low <= high:
            r.insert(mid, element)
        elif low == len(r):
            r.append(element)
        else:
            r.insert(low, element)
    return r

# Ejemplo de uso:
t = [5, 2, 9, 1, 6, 3]
sorted_t = binary_insertion_sort(t)
print("Tabla original:", t)
print("Tabla ordenada:", sorted_t)
