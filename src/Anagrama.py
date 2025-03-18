palabra1 = input("Palabra 1: ").lower().replace(" ", "")
palabra2 = input("Palabra 2: ").lower().replace(" ", "")
if sorted(palabra1) == sorted(palabra2):
    print("¡Son anagramas!")
else:
    print("No son anagramas.")
