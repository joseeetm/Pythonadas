# while ejecuta los pasos descritos siempre y cuando la condición dada sea true.
# Por ejemplo, hacer uso de 'while True' nos permite crear un loop infinito. Ya que un while True va a ser siempre true
# A veces es necesario hacer uso de un bucle infinito. Para procesos que necesitan ejecutarse todo el rato.

# Al ejecutar las siguientes líneas se genera un bucle infinito:

# while True:
#     print("Esto es un bucle infinito")

# A continuación se crea una variable con valor 1. Se indica que mientras que esta variable sea menor o igual a 4
# se imprima por consola la palabra "bucle" y se incrementa en 1 el valor de la variable. Resultando en que se
# imprime la palabra "bucle" 4 veces
count = 1
while count <= 4:
    print("Bucle")
    count += 1

# A continuación se crea un bucle para imprimir números impares menores a 10. Utilizando continue
count = 0  # Se empieza desde 0
while count < 10:  # Si la variable count es menor a 10. Se inicia el bucle
    if count % 2 == 0:  # Se comprueba si es múltiplo de 2.
        count += 1  # Al ser múltiplo de 2 se incrementa count en uno.
        continue  # Se continúa el bucle, sin volver a empezar (en este caso desde el valor 0 y se pasaría a 1. Luego a
        # 2 y luego a 3 comparando todo el rato.)
    print(f"Numero impar... {count}")  # Cuando la condición del if no sea true (es decir, que el valor de la variable
    # no es múltiplo de 2) se imprime el valor de la variable. Se utiliza print(f"") para poder imprimir el string de
    # la variable
    count += 1  # Se suma uno más tras imprimir el mensaje.

# Esta vez, en lugar de utilizar continue, se utiliza el opuesto que es break. Break funciona de manera contraria a
# continue, en cuanto la condición dada sea cierta, rompe el bucle.
count = 1  # Empezando en uno para que al menos salga un número
while count < 10:
    if count % 2 == 0:
        break  # En cuanto llega a 2 y es cierta la condición, se detiene el bucle.
    print(f"Contando impar... {count}")
    count += 1