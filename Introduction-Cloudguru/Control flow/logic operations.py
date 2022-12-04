# El operador 'not' devuelve lo opuesto a lo que resultaría cualquier otra condición
# Por ejemplo, bool("") devuelve false ya que no tiene valor
print(bool(""))  # Devuelve false
# Así al repetirlo con not devuelve true
print(not "")
# Lo mismo ocurre con una condición falsa como es el caso de '1' mayor que '2'...Devolverá true
print(not 1> 2)

# Not se puede utilizar con if.
if not 1 > 2:
    print("Aunque 1 sea menor que 2... La condición es true :V")
else:
    print("Si no estuviese el not, este sería el mensaje a devolver")

# Con 'or' si se compara un valor contenido con un valor falso devolverá el primer valor que sea verdadero
# Por ejemplo, se compara entre un string vacio y 'Jose'. Devuelve 'Jose' ya que es el primer valor verdadero.
print('' or 'Jose')

# Se declaran dos variables, una de ellas vacía y se comparan.
vacio = ""
lleno = "palabra"
if vacio or lleno:  # Imprime el mensaje
    print("Lleno está lleno")

# También se pueden definir variables haciendo comparaciones. Por ejemplo, se define una variable comparando su valor
# entre la variable previamente definida 'vacío' y un string.
estado = vacio or "semilleno"
# Como vacío devuelve false, el string es el valor de dicha variable.
print(estado)


# <------------ OPERADOR AND ------------------>
# Compara entre valores que estos deben de ser todos true para que la condición se dé como tal.
# Por ejemplo, se compara entre vacio y lleno. Devuelve false ya que vacío es false
if vacio and lleno:
    print("este mensaje no se va a imprimir")
else:
    print("Condición falsa")

