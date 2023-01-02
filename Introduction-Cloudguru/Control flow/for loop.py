# El bucle for se utiliza para recorrer elementos de un objeto iterable (lista,tupla, diccionario...) y ejecutar en cada
# uno una acción. Su sintaxis es "for <variable> in <iterable>". El for <variable> es el como se va a llamar a cada uno
# de los elementos del iterable. Normalmente la variable suele ser 'i'
# Por ejemplo. Se crea una lista que contiene el valor de los colores y se crea un bucle que imprime cada color
colores = ['azul','verde','rojo','amarillo']
for color in colores:
    print(color)  # Imprimirá por consola cada uno de los colores que hay

# Se crea un bucle para que solo imprima el color verde
for color in colores:
    if color == 'azul':  # Como el primer color es el azul, la condición es true y continúa el bucle al siguiente valor.
        continue
    elif color == 'rojo':
        break
    print(color)

# Su uso con las tuplas es el mismo
punto = (2.2, 3.0, 7)
for i in punto:
    print(i)
# También con diccionarios:
edades = {'kevin': 50, 'antonio': 40, 'fer': 34 }
for i in edades:
    print(f"{i} tiene {edades[i]}")

# También se puede tratar strings. Y los tratará como un tipo de secuencia por lo que irá por cada uno.
for i in "mi_string":
    print(i)

# También se puede jugar con tuplas. Se crea una tupla con una lista de puntos (x,y)
lista_de_puntos = [(1,2), (2,3), (3,4)]
# Se imprime cada valor de la tupla x e y por separado gracias al bucle.
for x, y in lista_de_puntos:
    print(f"x: {x}, y: {y}")

# También se puede asignar variables key:value a un diccionario mediante el método ".items()" ya que no se podría
# asignar dos variables pasando el diccionario entero.
for nombre, edad in edades.items():
    print(f"Persona llamada: {nombre}")
    print(f"Edad: {edad}")