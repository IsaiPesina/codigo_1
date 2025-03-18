# Lista de pizzas favoritas
pizzas = ["Pepperoni", "Hawaiana", "Cuatro Quesos", "BBQ Chicken", "Mexicana", 
          "Vegetariana", "Napolitana", "Margherita", "Suprema", "Champiñones", 
          "Tocino", "Carnes", "Al Pastor"]
print("Lista de pizzas favoritas:", pizzas)
print("Primera pizza:", pizzas[0])
print("Ultima pizza:", pizzas[-1])
pizzas.append("Diavola")
print("Después de agregar una pizza:", pizzas)
pizzas.insert(3, "Bacalao")
print("Después de insertar una pizza en la posición 3:", pizzas)
pizzas.remove("Hawaiana")
print("Después de eliminar 'Hawaiana':", pizzas)
ultima_pizza = pizzas.pop()
print(f"Después de eliminar la última pizza ({ultima_pizza}):", pizzas)
pizzas.sort()
print("Lista ordenada:", pizzas)
print("Lista en orden inverso:", pizzas)
print("Lista original después de sorted():", pizzas)
print("¿Cuántas veces aparece 'Napolitana'?", pizzas.count("Napolitana"))
print("Cantidad de pizzas en la lista:", len(pizzas))
for pizza in pizzas:
    print(f"Me encanta la pizza de {pizza}.")

