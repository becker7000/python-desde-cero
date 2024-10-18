from datetime import datetime, date

# Crear una fecha específica
fecha = date(2023, 10, 17)
print("Fecha específica:", fecha)

# Obtener la fecha actual
fecha_actual = date.today()
print("Fecha actual:", fecha_actual)

# Crear un objeto datetime
fecha_hora = datetime(2023, 10, 17, 14, 30)
print("Fecha y hora:", fecha_hora)

# Formatear la fecha actual
fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
print("Fecha formateada:", fecha_formateada)