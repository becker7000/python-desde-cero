import math

# Solicitar el radio del círculo al usuario
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área
area = math.pi * (radio ** 2)

# Mostrar el resultado
print(f"El área del círculo con radio {radio} es: {area:.2f}")
