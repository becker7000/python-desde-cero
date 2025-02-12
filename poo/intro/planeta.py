
class Planeta:

    def __init__(self,nombre, posicion, color):
        self.nombre = nombre
        self.posicion = posicion
        self.color = color

    def mostrar(self):
        print(f"""
               Nombre: {self.nombre}
               Posición: {self.posicion}
               Color: {self.color} 
            """)
