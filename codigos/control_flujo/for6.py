"""
    Crear un programa en Python
    que solicite un número entero:
    entonces, mostrar la tabla de multiplicar
    de ese número.
    Termina: 8:00 PM
"""

n = int(input("Escribe un número entero: "))
print(f"Tabla de multiplicar del {n}")

for i in range(1,11):
    print(f" {n} x {i} = {n*i}")
