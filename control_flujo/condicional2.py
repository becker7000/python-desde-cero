
# Guardamos una letra y la transformamos a minúscula...
letra = input("Escribe una letra: ").lower()

if letra in 'aeiou':
    print("La letra es una vocal")
else:
    print("La letra no es ninguna vocal")