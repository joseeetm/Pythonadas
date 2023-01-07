# Las funciones permite definir código para reusarlo sin tener que reescribirlo. Simplemente se nombra la función para
# poder utilizar el código de esta y con algún argumento/parámetro si procede. Se define con "def nombre_funcion: .... "
# Se define una función llamada hola_mundo
def hola_mundo():
    print("Hola, mundo!")
# Se ejecuta la función:
hola_mundo()
# Se crea otra función que imprime un nombre dado como un argumento.
def print_nombre(nombre):
    print(f"El nombre es {nombre}")
# Lo ejecutamos con el argumento/parámetro "Jose" y devuelve la frase "El nombre es Jose"
print_nombre("Jose")
# Se ejecuta de nuevo la función con el argumento "Berna", devuelve "El nombre es Berna"
print_nombre("Berna")

# No se puede guardar el resultado de nombrar una función en una variable, ya que por defecto una función
# no devuelven nada. Al definir la variable si que saldrá por pantalla el resultado pero no se almacena el valor.
output = print_nombre("No funciona")
# Devuelve un none
print(output)

# Para que una función devuelva algo, se ha de utilizar "return". En otras palabras, lo que nos permite que la función
# calcule algún valor y nos devuelva después dicho valor para poder utilizarlo después posteriormente.
# Se crea una función que hace un return del argumento sumándole 2
def sumar_dos(num):
    return num + 2
# Se crea una variable llamando a la función previamente definida asignando como argumento '5'
resultado = sumar_dos(5)
# Se imprime el contenido de la variable, lo que devuelve un 7 como resultado de la función.
print(resultado)

# Se pueden definir varios argumentos en una función. Por ejemplo, se crea una función llamada sumar
# que suma dos números
def sumar(num1,num2):
    return num1 + num2
# El resultado devuelve 35
print(sumar(20,15))
# Se crea otro ejemplo de función con tres argumentos.
def datos_personales(nombre,edad,coche):
    return f"{nombre} tiene {edad} años y conduce un {coche}"
# Se llama a la función dando tres argumentos. Lo que devuelve la frase "Jose tiene 20 años y conduce un Kia Rio"
print(datos_personales("Jose", 20, "Kia Rio"))
# Una manera alternativa de asignar un valor a los argumentos es definiendolos en vez de asignar el valor
# posicionalmente como en los ejemplos anteriores. El siguiente ejemplo
# devuelve: "Bernabé tiene 22 años y conduce un Peugeot 308"
print(datos_personales(nombre="Bernabé",edad=22, coche="Peugeot 308"))

# Se puede asignar un valor por defecto a los argumentos. Por ejemplo, se crea una función llamada 'can_drive' con dos
# argumentos, el primer argumento es 'edad' y el segundo será 'edad_requerida', predefinido a 18. Devolverá true si
# el argumento de la edad es mayor o igual al segundo argumento.
def can_drive(edad, edad_requerida=18):
    return edad >= edad_requerida
# Devuelve false ya que es menor que el segundo argumento predefinido.
print(can_drive(16))
# Sin embargo, LOS ARGUMENTOS PREDEFINIDOS SE PUEDEN MODIFICAR al asignar un segundo argumento. Por lo que se asigna
# a la función dos argumentos con el valor '16' y esta vez devuelve 'True'
print(can_drive(16,16))