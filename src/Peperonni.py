pizzas = ["Pepperoni", "Hawaiana", "Napolitana", "Cuatro Quesos", "BBQ Chicken",
          "Mexicana", "Vegetariana", "Margherita", "Suprema", "Champiñones",
          "Tocino", "Carnes", "Al Pastor"]
for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza}.")
pizzas.append("Diavola")  
print("\nLista actualizada de pizzas favoritas:", pizzas)
print("\nAplicando 13 métodos a la lista de pizzas:\n")
print("Primera pizza:", pizzas[0])
print("Última pizza:", pizzas[-1])
pizzas.insert(3, "Trufa")
print("Después de insertar 'Trufa' en la posición 3:", pizzas)

pizzas.remove("Hawaiana")
print("Después de eliminar 'Hawaiana':", pizzas)
ultima_pizza = pizzas.pop()
print(f"Después de eliminar la última pizza ({ultima_pizza}):", pizzas)
pizzas.sort()
print("Lista ordenada:", pizzas)
print("Lista en orden inverso:", pizzas)
print("Lista ordenada temporalmente:", sorted(pizzas))
print("Lista original después de sorted():", pizzas)
print("¿Cuántas veces aparece 'Napolitana'?", pizzas.count("Napolitana"))
print("Cantidad de pizzas en la lista:", len(pizzas))
print("¿Existe 'BBQ Chicken' en la lista?", "BBQ Chicken" in pizzas)
pizzas_copia = pizzas.copy()
print("Copia de la lista de pizzas:", pizzas_copia)
pizzas.clear()
print("Lista vaciada:", pizzas)
