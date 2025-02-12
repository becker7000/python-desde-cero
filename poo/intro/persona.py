
class Persona:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f" Hola, a todos soy {self.nombre} y tengo {self.edad} años... "
    
# Primero probar este código creando los objetos de la clase
# Persona dentro del archivo 
""" 
persona1 = Persona("Juan",20)
persona2 = Persona("Laura",19)

print(persona1.saludar())
print(persona2.saludar())
"""