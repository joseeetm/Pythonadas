# Los strings en Python se pueden tratar como listas (arreglos), donde cada posición tiene un índice
my_name = 'Jose'
first_initial = my_name[0]  # Se selecciona el primer carácter de 'Jose' usando el índice 0
print(first_initial)  # Imprime 'J'

# También podemos seleccionar partes de un string usando índices y slices (rebanadas)
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]  # Se seleccionan los primeros 5 caracteres de 'Villanueva'
print(new_account)  # Imprime 'Villa'

temp_password = last_name[2:6]  # Se seleccionan los caracteres desde el índice 2 hasta el 6 (no incluye el 6)
print(temp_password)  # Imprime 'llan'

# Esta función genera un nombre de cuenta uniendo los primeros 3 caracteres del nombre y apellido
def account_generator(first_name, last_name):
    account_name = first_name[:3] + last_name[:3]  # Toma los primeros 3 caracteres de cada nombre
    return account_name

new_account = account_generator('josegabriel', 'tirado')  # Genera una nueva cuenta usando 'jos' y 'tir'
print(new_account)  # Imprime 'jostir'

# Esta función genera una contraseña uniendo los últimos 3 caracteres del nombre y apellido
def password_generator(first_name, last_name):
    password = first_name[-3:] + last_name[-3:]  # Toma los últimos 3 caracteres de cada nombre
    return password

temp_password = password_generator(first_name, last_name)  # Genera una nueva contraseña usando 'igo' y 'eva'
print(temp_password)  # Imprime 'igoeva'

# Manipulando strings: obtenemos caracteres desde el final de la cadena usando índices negativos
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]  # Obtiene el segundo carácter desde el final ('f')
final_word = company_motto[-4:]  # Obtiene los últimos 4 caracteres ('life')

# Corrigiendo strings: reemplazamos el primer carácter de un nombre
first_name = "Bob"
last_name = "Daily"

fixed_first_name = 'R' + first_name[1:]  # Cambia la primera letra de 'Bob' a 'R'
print(fixed_first_name)  # Imprime 'Rob'

# String que contiene comillas escapadas (\" permite usar comillas dobles dentro del string)
password = 'theycallme\"crazy\"91'

# Esta función cuenta la longitud de una palabra recorriendo cada carácter y sumando 1 al contador
def get_length(variable):
    contador = 0
    for i in variable:  # Itera sobre cada carácter de la palabra
        contador += 1  # Incrementa el contador en 1 por cada carácter

    return contador  # Devuelve la longitud total de la palabra

print(get_length('tooooma'))  # Imprime la longitud de 'tooooma', que es 7


# Define la función letter_check que toma dos argumentos: word y letter
def letter_check(word, letter):
    # Inicializa un contador en 0
    counter = 0
    # Itera sobre cada carácter en la palabra
    for character in word:
        # Si el carácter es igual a la letra buscada, incrementa el contador
        if character == letter:
            counter += 1
    # Si el contador es mayor que 0, significa que la letra está en la palabra
    if counter > 0:
        return True
    else:
        return False

# Llama a la función letter_check con 'nabo' y 'p' y imprime el resultado
print(letter_check('nabo','p'))



# Define la función contains que toma dos argumentos: big_string y little_string
def contains(big_string, little_string):
    # Utiliza el operador 'in' para verificar si little_string está en big_string
    return little_string in big_string

# Llama a la función contains con 'nabazo' y 'naba' y imprime el resultado
print(contains('nabazo','naba'))



# Define la función common_letters que toma dos argumentos: string_one y string_two
def common_letters(string_one, string_two):
    # Inicializa una lista vacía para almacenar las letras comunes
    common_list = []
    # Itera sobre cada letra en string_one
    for letter in string_one:
        # Si la letra está en string_two y no está ya en common_list, añádela a common_list
        if letter in string_two and letter not in common_list:
            common_list.append(letter)
    # Retorna la lista de letras comunes
    return common_list

# Llama a la función common_letters con 'manhattan' y 'san francisco' y imprime el resultado
print(common_letters('manhattan', 'san francisco'))
