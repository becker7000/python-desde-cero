import math

# Solicitar al usuario los catetos
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))

# Calcular la hipotenusa
hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)

# Mostrar el resultado
print(f"La longitud de la hipotenusa es: {hipotenusa:.2f}")
