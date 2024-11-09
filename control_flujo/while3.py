import random

numero_oculto = random.randint(1,100)
intento = 0

while intento != numero_oculto:
    intento = int(input("Adivina el número entre 1 y 100: "))
    if intento < numero_oculto:
        print("Es mayor")
    elif intento > numero_oculto:
        print("Es menor")

print("Adivinaste el número...")