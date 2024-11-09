
segundos = int(input("Escribe los segundos: "))

# 4000 segundos -> 3600 (1 hora) + 360 (6 minutos) + 40 (40 segundos)
horas = segundos//3600
minutos = (segundos%3600)//60
segundos_sobrantes = segundos%60

print(f" {segundos} segundos equivalen a: ")
print(f" {horas} horas, {minutos} minutos, {segundos_sobrantes} segundos")