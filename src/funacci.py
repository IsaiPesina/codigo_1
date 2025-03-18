num = int(input("Ingrese la cantidad de términos de la serie Fibonacci: "))
a=0
b=1
print(a)
print(b)
contador = 2
while contador < num:
    fib = a + b
    print(fib)
    a, b = b, fib 
    contador += 1
