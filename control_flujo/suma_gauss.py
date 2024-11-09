
maximo = int(input("Sumar del 1 al: "))

contador = 1
suma = 0

while contador <= maximo:
    suma += contador
    contador += 1

print(f"La suma del 1 al {maximo} es: {suma}")