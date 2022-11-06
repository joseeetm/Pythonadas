# Un string es texto o números que se definen dentro de single quotes o doble quotes

#  No importa si es con una comilla
print('String con una comilla')
#  O doble quote, dos comillas
print("String con dos comillas")
# Con triple comilla simple ''' permite hacer definir un string multilínea
string='''
kmslkf
klsanfklja
lksanflka
'''
print(string)
# Se pueden realizar operaciones con dichos strings como multiplicaciones
multiplicarstring= 'Ha' * 4
print(multiplicarstring) # ! This returns HaHaHaHA

# ! Se pueden sumar strings
concat= 'hola' + 'soperra'
print(concat)  # ! Esto devuelve 'holasoperra'

#  Existen lo que se conoce como 'string methods' que son estilos de formatear strings

#  En la siguiente línea se muestra el método find, que permite encontrar un caracter
#  dentro un string. EL resultado es la posición de dicho string de izquierda a derecha.
#  Si no lo encuentra, devuelve un valor negativo.
print(concat.find('q'))  # Devuelve valor negativo ya que no existe la q
print(concat.find('p'))  # Devuelve el valor 6 ya que la p está en sexta posición

# Para formatear texto convirtiéndolo en minúsculas se usa lower()
palabra= 'GoD DaMmIt'
print(palabra.lower())  # Se imprime la palabra en minúscula

# El método inverso es pasar a mayúsculas con upper()
print(palabra.upper())  # Se devuelve en mayúsculas

# Existen escape characters. Con \t se añade una tabulación
print('hola\tamigo')  # Devuelve 'hola   amigo'

# Con \n se agrega un salto de línea
print('linea1\nlinea2')  # Devuelve linea 1 en una línea y linea 2 en la otra

# Para imprimir un backslash se ha de poner doble backslash ya que si has escrito
# un scape character, se realizará dicha acción. Por ejemplo al querer escribir viejo\nuevo
print('viejo\nuevo')  # Se escribirá nuevo sin la 'n' y además en otra línea

# Se repite con \\ y ahora si funciona
print('viejo\\nuevo')

# Si se quisiese añadir doble quotes en el print se puede sin problemas. Se entrecomilla con ' '
print('Me dijo "hola"')

# Pero para poner comillas simples habrá que escaparlas con backslash
print('Me dijo \'hola\'')