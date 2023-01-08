# Los diccionarios son un tipo de sequencias utilizadas para almacenar datos en pairs key:value
# Los diccionarios en vez de tener índices basados en la posición, como las listas y tuplas. Tienen
#  'named index' o index nominativos.
# La sintaxis de los diccionarios es {'key':value,'key':value,...}. UN DICCIONARIO NO PUEDE TENER KEYS REPETIDAS

# Se crea un diccionario de edades. Donde cada clave es el nombre de la persona y el valor su edad.
edades = {'Josetm':20,'Pablo':20,'Josemi':21,'Berna':22}
print(edades)
# Para consultar el contenido de una key de un diccionario, se hará partiendo de una key de este y
# se obtendrá el value de vuelta.

# En este caso, se consulta el valor de la key 'Josetm'
print(edades['Josetm'])

# Los diccionarios si son mutables. Es decir, se pueden modificar añadiendo, modificando o eliminando valores.
# Se inserta el valor 'Isra' con valor 20
edades ['Isra'] = 20
print(edades)
# Se modifica dicho valor a 21
edades ['Isra'] = 21
print(edades)

# Se pueden eliminar valores con la función del. Se elimina el valor de Isra
del edades['Isra']
print(edades)
# Hay que ser cuidadoso al utilizar esta función ya que puede eliminar variables enteras. Es decir, es capaz de eliminar
# todo el diccionario.
del edades
# La siguiente línea daría un error ya que se ha elimindo el diccionario entero tras la línea anterior
# print(edades)
# Se vuelve a crear el diccionario
edades = {'Josetm':20,'Pablo':20,'Josemi':21,'Berna':22}
# El método pop() con diccionarios funciona igual que las listas pero en vez de hacer referencia a un index, se hace
# referencia al key.
# Se elimina la clave Berna
edades.pop('Berna')
print(edades)

# Una alternativa para obtener el valor de una key es con el metodo get()
print(edades.get('Josetm'))
# La diferencia que tiene el método get es que no dá error en caso de que no exista la key buscada.
# A diferencia de obtener el value mediante diccionario[key] que si causa un error cuando el key no existe
# Se elimina el key de josetm
edades.pop('Josetm')
# La siguiente línea generaría un error ya que el key no existe ya
# print(edades['Josetm'])
# En cambio, con el método get simplemente devuelve un none en caso de que la key no exista en vez de causar un error.
print(edades.get('Josetm'))

# El método keys() devuelve los keys de un diccionario:
print(edades.keys())
# También se pueden sacar las keys en forma de lista
print(list(edades.keys()))

# El método values() devuelve los valores de un diccionario.
print(edades.values())
# También se pueden sacar las keys en forma de lista
print(list(edades.values()))

# Otra manera de crear diccionarios es con la función dict().
# La primera sintaxis de crear un diccionario con dict() es dict(key=value,key=value...)
pesos = dict(jose=81, manu=65)
print(pesos)
# Otra sintaxis para utilizar la función dict() es mediante el uso de una lista de tuples
colores = dict([('Jose','verde'), ('Manu','rosa')])
print(colores)