from datetime import datetime

# Guardamos una cadena que contiene una fecha con formato
fecha_nacimiento = input("Escribe tu fecha de nacimiento: (formato: dd/mm/aaaa): ")

# Convertimos la cadena a fecha:
fecha_nacimiento = datetime.strptime(fecha_nacimiento,"%d/%m/%Y")

# Fecha actual:
fecha_act = datetime.now()

# Calculamos la diferencia entre las fechas:
diferencia = fecha_act - fecha_nacimiento

# Calculos para años, meses y días
anios = diferencia.days//365
meses = (diferencia.days%365)//30
dias = (diferencia.days%365)%30

print(f" Tienes {anios} años, {meses} meses y {dias} días...")

