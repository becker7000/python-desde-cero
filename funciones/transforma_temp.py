
def celsius_fahrenheit(celsius):
    return celsius * 1.8+32

def celsius_kelvin(celsius):
    return celsius + 273.15

celsius = float(input("Escribe los °C: "))

print(f" {celsius:.3f} °C equivalen a {celsius_fahrenheit(celsius):.3f} °F")
print(f" {celsius:.3f} °C equivalen a {celsius_kelvin(celsius):.3f} °K")

# Crear una función que transforme grados Celsius a grados Kelvin (8:21 PM)
# Terminar las otras 4 transformaciones
# De °F a °C
# De °K a °C
# De °F a °K
# De °K a °F
