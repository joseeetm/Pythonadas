# Script para ordenar una lista usando el algoritmo "Booble sort"
print('--- Bienvenido al script de josetm del algoritmo booble sort ---')

lista_desordenada = [8, 3, 12, 1, 7, 9, 4, 11, 6, 2, 10, 5]


print('Esta es la lista desordenada', lista_desordenada)


def booble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Como con cada pasada el valor más grande se va a quedar a la derecha del todo,
        #  nos quedamos en una menos en las siguientes
        for j in range(0, n-i-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista_ordenada = booble_sort(lista_desordenada)

print('Esta es la lista ordenada con el algoritmo booble sort:', lista_ordenada)