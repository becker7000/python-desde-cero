
suma = 0

# Generando un ciclo infinito
while True:
    z = int(input("Escribe un entero (0 para terminar): "))
    if z==0:
        break
    suma+=z

print(f"La suma total es: {suma}")
