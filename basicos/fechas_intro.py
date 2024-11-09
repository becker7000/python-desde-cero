from datetime import datetime, date

# Creando una fecha especifica:
fecha = date(2023,10,20)
print("Fecha especifica: ",fecha)

# Creando la fecha actual
fecha_actual = date.today()
print("Fecha actual: ",fecha_actual)

# Creando un objeto de datetime
fecha_hora = datetime(2020,11,15,14,30)
print(f" Fecha y hora: {fecha_hora} ")

# Hora actual:
hora_actual = datetime.now().time()
print(f" La hora actual es: {hora_actual}")

# Formatear la fecha actual
# %y -> año a dos dígitos
fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
print("Fecha actual formateada: ",fecha_formateada)
