
def es_par(num):
    return num % 2 == 0

def es_impar(num):
    return num % 2 == 1

n = int(input("Escribe un número entero: "))

if es_par(n):
    print("El número es par")

if es_impar(n):
    print("El número es impar")

# Agregar es_impar