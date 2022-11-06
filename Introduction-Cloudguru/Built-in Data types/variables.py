# Definir variable y valor de string
nombre = 'Jose'
print(nombre)
# Podemos imprimir variables y concatenarle cosas
print(nombre + " Gabriel")
# Para poder añadir valor a la variable se hace con +=
nombre += ' Gabriel'
print(nombre)
# Otra manera es renombrar la variable autonombrando dicha variable y concatenando
nombre = nombre + ' Tirado'
print(nombre)
# También otra forma es concatenar el resultado de otra variable
segundoapellido = ' Márquez'
nombre += segundoapellido
print(nombre)

# También se puede igualar una variable al contenido de otra.
# Por ejemplo, se tienen dos variables. Un string y un integer.
my_str = "Jose"
my_int = 6
# Se iguala el valor del string al integer
my_str = my_int
print(my_str)

