# Función para convertir Fahrenheit a Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

# Convertir 100 Fahrenheit a Celsius y almacenar el resultado
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Función para convertir Celsius a Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * 9/5 + 32
    return f_temp

# Convertir 0 Celsius a Fahrenheit y almacenar el resultado
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Definición de variables para masa, aceleración y distancia del tren, y masa de la bomba
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Función para calcular la fuerza (F = m * a)
def get_force(mass, acceleration):
    return mass * acceleration

# Calcular la fuerza del tren y almacenarla
train_force = get_force(train_mass, train_acceleration)
print(f'The GE train supplies {train_force} Newtons of force.')

# Función para calcular la energía (E = m * c^2)
def get_energy(mass, c=3*10**8):
    return mass * c**2

# Calcular la energía de la bomba y almacenarla
bomb_energy = get_energy(bomb_mass)
print(f'A 1kg bomb supplies {bomb_energy} Joules')

# Función para calcular el trabajo (W = F * d)
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

# Calcular el trabajo realizado por el tren y almacenarlo
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f'The GE train does {train_work} Joules of work over {train_distance} meters')
