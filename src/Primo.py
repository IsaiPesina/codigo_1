num = int(input("Ingrese un número: "))
if num < 2:
    print("No es un número primo.")
else:
    es_primo = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            es_primo = False
            break
        i += 1
    if es_primo:
        print("Es un número primo")
    else:
        print("no es un número primo")
