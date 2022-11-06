# Se pueden hacer comparaciones con distintos símbolos de comparación, lo cuál Python devolverá si dichas comparaciones
# son verdaderas o falsas
# Se compara si 1 es menor que 2, lo que es true
print(1 < 2)
# Se compara si 1 es mayor que 2, lo que es false
print(1 > 2)
# Se compara si 1 es mayor o igual a 2, lo que es false
print(1 >= 2)
# Se compara si 1 es igual a 2, lo que es false
print(1 == 2)
# Se compara si 1 es igual a 1, lo que es true
print(1 == 1)
# Se compara si 1 es igual a 1.0, lo que es true
print(1 == 1.0)
# Se compara si 'b' es igual a 'b', lo que es true
print('b' == 'b')
# En cambio al comparar si 'b' es igual a 'B' es false
print('b' == 'B')
# Se puede comparar si un string y un float o int es igual. Pero no si es mayor o menor
print(3.1 == 'this')
# La siguiente línea daría error ya que se estaría comparando si un float es mayor que un string.
# print(3.1 >= 'this')

# Se pueden hacer comparaciones entre strings.
# Se compara si a es mayor que b, lo que es false
print('a' > 'b')
# Se compara si b es mayor que a, lo que es true
print('b' > 'a')

#