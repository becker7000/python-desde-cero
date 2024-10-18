from datetime import datetime

# Solicitar la fecha de nacimiento al usuario
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (formato: dd/mm/yyyy): ")

# Convertir la cadena de fecha a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular la diferencia
diferencia = fecha_actual - fecha_nacimiento

# Calcular años, meses y días
anos = diferencia.days // 365
meses = (diferencia.days % 365) // 30
dias = (diferencia.days % 365) % 30

# Mostrar el resultado
print(f"Tienes {anos} años, {meses} meses y {dias} días.")
