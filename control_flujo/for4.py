
# Lista de números:
reales = [50.5,78.3,28.6,120.9,80.5]

promedio = 0.0

for x in reales:
    promedio += x

promedio /= len(reales)

print(reales)
print(f" El promedio de los {len(reales)} números reales es: {promedio} ")