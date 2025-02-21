# biblioteca.py
from libro import Libro
from miembro import Miembro

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.__str__()}' agregado a la biblioteca.")
    
    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)
        print(f"Miembro '{miembro.get_nombre()}' agregado a la biblioteca.")
    
    def listar_libros(self):
        print("Libros disponibles en la biblioteca:")
        for libro in self.libros:
            print(libro)
    
    def listar_miembros(self):
        print("Miembros registrados:")
        for miembro in self.miembros:
            print(miembro)
