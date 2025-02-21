# bibliotecario.py
from persona import Persona

class Bibliotecario(Persona):
    def __init__(self, nombre, edad, id_empleado):
        super().__init__(nombre, edad)
        self.__id_empleado = id_empleado  # Identificador único del bibliotecario
    
    def registrar_libro(self, libro):
        # Método para registrar un libro en la biblioteca
        print(f"El bibliotecario {self.get_nombre()} ha registrado el libro: {libro.get_titulo()}")

    def eliminar_libro(self, libro):
        # Método para eliminar un libro de la biblioteca
        print(f"El bibliotecario {self.get_nombre()} ha eliminado el libro: {libro.get_titulo()}")

    def __str__(self):
        return f"{super().__str__()}, ID Empleado: {self.__id_empleado}"
