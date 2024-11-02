import math

cateto_a = float(input("Escribe el cateto a: "))
cateto_b = float(input("Escribe el cateto b: "))

hipo = math.sqrt(cateto_a**2+cateto_b**2)

print(f" La longitud de la hipotenusa es: {hipo:.3f} ")