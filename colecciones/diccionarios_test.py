
# Diccionario vacío:
estudiantes = {}

# Agregamos dos claves
estudiantes["Roberto"] = []
estudiantes["Karla"] = []

# Añadimos calificaciones a los estudiantes:
estudiantes["Roberto"].append(85)
estudiantes["Roberto"].append(95)
estudiantes["Karla"].append(78)
estudiantes["Karla"].append(98)

print(estudiantes)

for nombre,notas in estudiantes.items():
    if notas:
        promedio = sum(notas)/len(notas)
        print(f"Alumno: {nombre}, promedio: {promedio:.2f}")
    else:
        print(f"El estudiante {nombre} no tiene calificaciones aún")
