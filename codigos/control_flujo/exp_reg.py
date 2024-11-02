import re

num_tel = input("Escribe un número telefonico: ")
patron = re.compile(r'^[0-9]{10}$')

if patron.match(num_tel):
    print("El teléfono es válido (cumple con su expresión regular)")
else:
    print("El teléfono NO es válido...")
