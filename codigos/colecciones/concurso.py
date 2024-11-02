
# Usando listas:
nombres = []
puntuaciones = []

numero_concursantes = int(input("Escribe el número de jugadores: "))

for x in range(numero_concursantes):
    nombre = input("Nombre: ")
    puntuacion = int(input("Puntuación: "))
    nombres.append(nombre)
    puntuaciones.append(puntuacion)

for i in range(len(nombres)):
    print(f" Jugador: {nombres[i]} - puntuación: {puntuaciones[i]} ")