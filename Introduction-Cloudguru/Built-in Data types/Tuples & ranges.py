# Un tuple es una secuencia inmutable.
# Es decir, una vez que se define dicho objeto no puede ser sujeto a modificaciones.
punto = (2.0, 3.0)
# Se pueden sacar index de la tupla
print(punto[0])
# En ningún caso se podría asignar otros valores ya que es inmutable,
# no permite la asignación de por lo que la siguiente línea si se descomenta dá error.
# punto[0] = 1

# Aunque el contenido de las tuples no se pueda modificar, si que se puede operar con estos valores.
# Por ejemplo, se crea la tupla 'punto3d' que será el valor de 'punto' pero añadiendo un 4.0. Será importante
# que se añada una coma en caso de ser un único valor como es el caso para que se interprete como un tuple de
# único item y no como una operación aritmética.
punto3d = punto + (4.0,)
print(punto3d)

# Otra opción que se permite es desempaquetar los valores del tuple. En este ejemplo se desempaquetan los tres
# valores de punto3d y se asignan a tres letras
x, y, z = punto3d
# Primer valor de la tuple 'punto3d'
print(x)
# Segundo valor de la tuple 'punto3d'
print(y)
# Tercer valor de la tuple 'punto3d'
print(z)

# Otro de los usos de los tuples es con la sustitución de sus valores. Con %s se sustituye por el valor de un string
# Por ejemplo, se agrega a la frase "Mi nombre es %s %s" junto una tupla con dos valores que serán sustituidos por
# el metacaracter
print("Mi nombre es: %s %s" % ("Jose", "TM"))
# Estos metacaracteres no pueden ser utilizados más veces que valores haya en la tupla.
# Así la siguiente línea daría un error.
# print("Mi nombre es: %s %s %s" % ("Jose", "TM"))

# De la misma forma, si no se sustituyen todos los argumentos de la tuple, también será erróneo.
# Por lo que la siguiente línea tampoco funcionará
# print("Mi nombre es: %s %s" % ("Jose", "gran", "TM"))

# Los rangos permiten crear una sequencia de números desde un número incial a uno final. Sigue la misma sintáxis
# que el slicing de listas, es decir range(start, stop, step. A continuación se crea un rango de los primeros 10 números
# Empezando por el 0 ya que no le asignamos valor start
print(range(10))
# Se puede imprimir todos los valores del range utilizándolo en una lista. El resultado serán los primeros 10 valores,
# es decir, del 0 al 9. Ya que el valor start será 0 al no asignarle ninguno
print(list(range(10)))
# No hay límite en esto, podemos crear rangos de la cantidad que queramos, incluso de 10.000 números.
print(range(10000))
# Se sacan 10.000 números del 0 a 10.000
print(list(range(10000)))

# Como ya se fijo, sigue la sintáxis del slicing, por lo que se le puede meter steps.
# Por ejemplo se crea un rango del 1 al 12 con salto de 2 valores.
print(range(1,12,2))
# Se imrime por pantalla todos los valores del rango
print(list(range(1,12,2)))