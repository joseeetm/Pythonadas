# Se declaran listas con []
lista = [1,2,3,4,5]
# Se puede hacer referencia a uno de los valores de la lista con lista[n]
print(lista[0])  # Imprime un 1 puesto que se empieza a contar desde 0.
print(lista[1])  # Imprime un 2 puesto que es la segunda posición y la primera la ocupa el 0
print(lista[3])  # Imprime un 4
# Con la función len se devuelve la longitud de una cadena cuando se aplica a strings.
# cuando es a un objeto (en este caso una lista), se refiere a la cantidad de items que hay en una lista.
# Así te aseguras de que no vas a intentar sacar un indice que exceda el número de items que tiene.
print(len(lista))
# En el ejemplo de abajo se obtiene la última posición. Ya que siempre va a ser el número total - 1
print(lista[len(lista) - 1])
# Otra manera es poner el número del índice en negativo y se comenzará desde el final
print(lista[-1])
print(lista[-2])
# Con : se puede sacr un rango de la lista, desde la posición x:y.
# En el siguiente ejemplo se muestra como sacar desde la posición 0 a la 2.
# Sin incluir el segundo index, es decir, sacará las posiciones 0 y 1, pero no el 2. A esto se le llama slicing
print(lista[0:2])
# En este ejemplo se saca desde la posición 2 hasta la 4. Es decir, solo saca la posición 2 y 3
print(lista[2:4])
# En cambio si se prescinde del último elemento se está diciendo la posición de inicio pero no de cierre.
# Por lo que se obtendrá del inicio al final
print(lista[2:])
# El formato de slicing es (start:stop:step). Este último campo añade n saltos de posiciones con cada secuencia.
# Se parte de la posición 0 (el 1), luego lo imprime. Se realiza un salto de 2 items,
# por lo que se saca la posición 2 (número 3
print(lista[::2])
# Se puede incluso asignar un step negativo. En ese caso devuelve la lista desde el final al inicio
print(lista[::-1])

# Es posible modificar un item de una lista. Ya que las listas son mutables
# Simplemente se nombre el index y se modifica el valor
# A continuación se cambia el primer item de 1 a 'a' y al volver a sacar por pantalla los valores de la lista.
# se observa como efectivamente se ha efectuado el cambio.
lista[0] = 'a'
print(lista)
# También se puede modificar rangos de items. Por ejemplo se modifican los dos primeros y se sustituyen por una 'a'
lista[0:2] = 'a'
print(lista)
# También es aplicable para eliminar un rango de items. En este caso se eliminan los dos primeors items.
lista[0:2] = []
print(lista)

# Para modificar el contenido de las listas existen funciones como alternativa a los ejemplos anteriores.
# La función remove() permite eliminar un item concreto (se filtra por valor, no posición).
# Por ejemplo se elimina el item con valor '5'
lista.remove(5)
print(lista)

# Se devuelven los valores de la lista
lista = [1,2,3,4,5]

# La función pop(x) a diferencia de remove() elimina el item indicado en la posición x
lista.pop(0)
print(lista)

# Para agregar un item al final de la lista se utiliza la función append(x). Siendo x el valor a agregar
lista.append('Gibraltar')
print(lista)

# Se puede insertar items en una posición específica con insert( index, item).
# Por ejemplo, se añade el string 'inicio' a la primera posición
lista.insert(0,'inicio')
print(lista)
