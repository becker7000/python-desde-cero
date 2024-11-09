
a = int(input("Calcular el factorial de: "))

n = a
factorial = 1

while a > 1:
    factorial *= a
    a -= 1

print(f" {n}! = {factorial}")

# 4! = 4*3*2*1 = 24
# 5! = 5*4*3*2*1 = 120

"""
    Ejercicio tarea:
    Solicitar un número entero (ejemplo 100)
    entonces sumar del 1 hasta ese número 
    es decir, la suma de Gauss
"""