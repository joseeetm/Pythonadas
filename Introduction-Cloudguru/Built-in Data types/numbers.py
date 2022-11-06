# los números al no ser strings, si no integers, van sin comillas cuando se desea operar con ellos
# suma
print(2+5)
# resta
print(40-32)
# También se puede operar con números negativos
print(-4.343 + 2)
# multiplicación
print(3*2)
# división
print(5/3)
# Función de parte entera ó floor división con // . División sin decimales.
print(5//3)
# Para obtener el resto se utiliza %
print(5%3)
# Para elevar números se hace con ** ó con la función pow(base,exponente)
print(2**3)
print(pow(2,3))

# Las operaciones con decimales se distinguen con '.'. Esta operación convierte de integer a float
print(1.1 + 3.1)
# Será indiferente que la operación sea limpia y dé un número entero, será float en el momento que se meta un decimal.
print(1.0+2)  # Devuelve un float

# Se puede pasar un número a string mediante str()
numerofloat = 1.0 + 2.5
print(str(numerofloat))
# Y también pasar a float
print(float(numerofloat))
# La variable siguiente contiene un string
numerostring = '3489'
# Con la función int() pasamos el dato a integer
print(int(numerostring))
# Cuando son dos integers podemos operar con ellos
numerostring2 = '2399'
print(int(numerostring) + int(numerostring2))
#Para saber el tipo de data que contiene una variable se utiliza type()
print(type(numerostring))  # Dirá que es un string
numerostring = int(numerostring)
print(type(numerostring))  # Ahora dirá que es un integer porque lo hemos cambiado a integer
# Se hace igual pero esta vez a float
numerostring = float(numerostring)
print(type(numerostring))
# Se devuelve a string
numerostring = int(numerostring)
print(type(numerostring))
