# Define la función username_generator que toma dos argumentos: first_name y last_name
def username_generator(first_name, last_name):
    # Verifica si la longitud de first_name es menor que 3 o la longitud de last_name es menor que 4
    if len(first_name) < 3 or len(last_name) < 4:
        # Si alguna de las condiciones es verdadera, usa los nombres completos para el username
        username = first_name + last_name
    else:
        # Si ambas condiciones son falsas, toma los primeros 3 caracteres de first_name y los primeros 4 de last_name
        username = first_name[:3] + last_name[:4]
    # Retorna el username generado
    return username

# Llama a la función username_generator con 'Abe' y 'Simpson' y imprime el resultado
print(username_generator('Abe', 'Simpson'))

# Define la función password_generator que toma un argumento: user_name
def password_generator(user_name):
    # Inicializa una variable password con el último carácter de user_name seguido del resto de user_name menos el último carácter
    password = user_name[-1] + user_name[:-1]
    # Retorna el password generado
    return password

# Llama a la función password_generator con 'nabo' y imprime el resultado
print(password_generator('nabo'))
