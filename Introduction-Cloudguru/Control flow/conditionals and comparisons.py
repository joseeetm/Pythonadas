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
# Se compara si 'a' es distinto a 'b', lo que es true
print('a' != 'b')
# Se compara si 3,1 es distinto a 'this' lo que es true
print(3.1 != 'this')

# En la comparación de strings de distinta longitud, va a comparar carácter por carácter.
# En caso de empate pasa al siguiente caracter.
# Así por ejemplo 'abc' es menor que b lo que es true. Ya que 'a' es menor que 'b'
print('abc' < 'b')
# Ahora, sin embargo, al comparar si 'bac' es menor que 'b' se obtiene que es false ya que hay empate con 'b' y 'b'
# y se pasa al siguiente caracter devuelve false ya que 'a' es mayor que un caracter no existente
print('bac' < 'b')

# Con 'in' se permite comparar si 'x' valor está presente en el contenido de un objeto.
# Se compara si existe el número '2' en una lista. Devuelve true ya que el '2' se encuentra en la lista
print(2 in [1,2,3])
# Ahora se compara si existe el número '4', lo que devolverá false ya que no se encuentra en la lista
print(4 in [1,2,3])

# El operador opuesto es 'not in' que funciona del modo opuesto a 'in'. Compara si NO existe 'x' valor en
# el contenido de un objeto. Se repiten los mismos ejemplos anteriores y devuelven el resultado opuesto.
# Se compara si NO existe el número '2' en una lista. Devuelve false ya que el '2' está en la lista
print(2 not in [1,2,3])
# Ahora se compara si NO existe el número '4', lo que devolverá true ya que no se encuentra en la lista
print(4 not in [1,2,3])

# *****----------------Condicionales-------------********
# Con if se verificará si la condición dada es verdadera y ejecutar el bloque que se le indique.
# Después de la condición ha de finalizar con ':' y el código a ejecutar debe estar en la siguiente línea
# con 4 espacios de separación
if True:
    print('Era verdadero')
# Otro ejemplo comparando si 1 es mayor que dos. Al ser la condición false, no devolverá el mensaje del print
if 1 > 2:
    print("Esto no va a funcionar")

# Se repite el ejemplo, esta vez la condición es que '1' es menor que '2' y por tanto se imprimirá el mensaje.
if 1 < 2:
    print("Es verdadero")
    print("Obviamente 1 es menor que 2")

# El siguiente operador a utilizar será 'else' que se utilizará para declarar el código que se ejecutará en caso de
# la condición sea errónea.
if 1 > 2:
    print("Este no va a salir")
else:
    print("Este si sale porque la condición es falsa")

# Hasta ahora con if y else solo podemos tener una condición. Para añadir múltiples condiciones en caso de que la
# principal sea falsa, se utiliza elif para añadir otra condición. Podemos poner tantas condiciones como queramos.
nombre = "Jose"
if len(nombre) >= 6:  # Se compara si la longitud de 'Jose' es mayor o igual a 6 por lo que la condición es falsa.
    print("El nombre es mayor o igual a 6 letras")
elif len(nombre) == 5:  # Al ser la condición principal falsa, se realiza la siguiente condición.
    print("El nombre tiene 5 letras")
elif len(nombre) == 4:  # Al ser la condición del anterior elif falsa. Se realiza esta condición que si será true.
    print("El nombre tiene 4 letras")  # Al ser true la condición del elif. Se imprime este mensaje
else:
    print("El nombre tiene menos de 4 letras")
