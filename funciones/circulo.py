import math

def calcular_area(radio):
    return math.pi * radio ** 2

def calcular_perimetro(radio):
    return math.pi * radio * 2

def calcular_diametro(radio):
    return radio * 2

radio = float(input("Escribe el radio: "))

print(f" El área del círculo es: {calcular_area(radio):.3f}")
print(f" El perímetro del círculo es: {calcular_perimetro(radio):.3f}")
print(f" El diametro del círculo es: {calcular_diametro(radio):.3f}")

# Agregar calcular_perimetro (7:29)
# Agregar calcular_diametro