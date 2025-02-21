# miembro.py
from persona import Persona

class Miembro(Persona):
    def __init__(self, nombre, edad, id_membresia):
        super().__init__(nombre, edad)
        self.__id_membresia = id_membresia
        self.__libros_prestados = []

    def get_id_membresia(self):
        return self.__id_membresia

    def set_id_membresia(self, id_membresia):
        self.__id_membresia = id_membresia
    
    def get_libros_prestados(self):
        return self.__libros_prestados

    def prestar_libro(self, libro):
        if len(self.__libros_prestados) < 5:
            self.__libros_prestados.append(libro)
            print(f"{self.get_nombre()} ha prestado el libro: {libro.get_titulo()}")
        else:
            print("Límite de libros prestados alcanzado.")
    
    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)
            print(f"{self.get_nombre()} ha devuelto el libro: {libro.get_titulo()}")
        else:
            print(f"{self.get_nombre()} no tiene este libro.")
    
    def __str__(self):
        return f"{super().__str__()}, ID Membresía: {self.__id_membresia}"
