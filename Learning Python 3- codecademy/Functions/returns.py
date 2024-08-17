# Establece el presupuesto inicial para el viaje.
current_budget = 3500.75

# Define una función para imprimir el presupuesto restante.
def print_remaining_budget(budget):
  # Imprime el presupuesto restante, convirtiendo el número a string para poder concatenarlo.
  print("Your remaining budget is: $" + str(budget))

# Llama a la función `print_remaining_budget` para mostrar el presupuesto inicial.
print_remaining_budget(current_budget)

# Aquí empieza la sección donde vas a escribir tu código.
# Define una función para deducir un gasto del presupuesto.
def deduct_expense(budget, expense):
  # Calcula el presupuesto restante después de deducir el gasto.
  subtract = budget - expense
  # Devuelve el nuevo presupuesto.
  return subtract

# Ejemplo de cómo llamar a `deduct_expense` y imprimir el resultado directamente.
print(deduct_expense(current_budget, 200))

# Establece el costo de una camiseta como un gasto.
shirt_expense = 9

# Calcula el nuevo presupuesto después de comprar la camiseta.
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

# Imprime el presupuesto restante después de la compra de la camiseta.
print_remaining_budget(new_budget_after_shirt)
