numeros_pares = []
cantidad = int(input("¿Cuántos numeros quieres ingresar?: "))
contador = 0
while contador < cantidad:
    num = int(input(f"Ingrese un número: "))
    if num % 2 == 0:
        numeros_pares.append(num) 
    contador += 1 
print("Lista de números pares que ingresaste:", numeros_pares)
