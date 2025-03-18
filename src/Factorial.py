def factorial(N):
    resultado = 1
    contador = 1 
    while contador <= N:
        resultado *= contador  
        contador += 1
    return resultado

num = int(input("porfavor dame un numero para caluclar la factorial: "))
if num < 0:
    print("el factorial no es definido como numero negativo")
else:
    print(f"El factorial de {num} es: {factorial(num)}")
