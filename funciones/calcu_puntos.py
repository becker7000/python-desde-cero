import math

def distancia_puntos(x1,y1,x2,y2):
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

def pendiente_puntos(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1) # Validar el caso en el que el divisor es cero

# Crear una función que calcule el punto medio entre dos puntos

x1 = float(input("x1: "))
y1 = float(input("y1: "))

x2 = float(input("x2: "))
y2 = float(input("y2: "))

print(f" Punto 1: ({x1},{y1})")
print(f" Punto 2: ({x2},{y2})")

print(f"La distancia entre el punto 1 y 2 es: {distancia_puntos(x1,y1,x2,y2)} ")
print(f"La pendiente entre el punto 1 y 2 es: {pendiente_puntos(x1,y1,x2,y2)} ")

# Crear una función que calcule la pendiente entre dos puntos
# Termina a las 8:51 PM