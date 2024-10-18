# Solicitar al usuario la cantidad de segundos
segundos = int(input("Ingresa el número de segundos: "))

# Calcular horas, minutos y segundos
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

# Mostrar el resultado
print(f"{segundos} segundos son equivalentes a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
