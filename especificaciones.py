# Algoritmo SIN tabla auxiliar:

# Entrada:
# t: TABLA[ENTEROS][1,n] escogidos de manera aleatoria
# t es una tabla de enteros desordenada
# inicio: posición inicial del segmento a explorar
# fin: posición final del segmento a explorar

# Precondición:
# los elementos de t son de tipo enteros, es decir, comparables
# el número de elementos de t tiene que ser impar
# inicio y fin son enteros válidos que representan un segmento dentro de la tabla

# Procedimiento de cálculo:

'''Guarda el primer elemento del segmento.
Elimina el primer elemento del segmento.
Desplaza los elementos restantes una posición hacia la izquierda.
Coloca el elemento guardado al final del segmento.
Verifica si el segmento está ordenado correctamente, comparándolo con una versión ordenada 
descendente del mismo.
Retorna True si el segmento está explorado (ordenado correctamente), False de lo contrario'''

# Fin de esta_explorado

# Poscondición:
# El segmento de la tabla t ha sido explorado según las reglas establecidas

# Salida:
# True si el segmento está explorado, False en caso contrario'''


# Función que verifica si esta explorado el segmmento de una tabla
def esta_explorado(t, inicio, fin):
    
    # primero identificamos el primer elemento del segmento
    primer_elemento = t[inicio]
    
    # se elimina el primer elemento del segmento
    del t[inicio]
    
    # Desplazamos los elementos del segmento una posición hacia la izquierda
    for i in range(inicio, fin):
        t[i] = t[i+1]
    
    # Se coloca el elemento eliminado en la última posición del segmento
    t[fin] = primer_elemento
    
 
    # Verificar si el segmento está "explorado"
    segmento_ordenado = sorted(t[inicio: fin+1], reverse=True)
    return t[inicio: fin+1] == segmento_ordenado


# Ejemplo de uso
tabla = [1, 2, 3, 9, 4, 5, 6, 7, 8, 10, 12]
inicio = 3
fin = 7

explorado = esta_explorado(tabla, inicio, fin)
print("¿Está explorado?", explorado)
print("Tabla reordenada:", tabla)


