# libro.py
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = True

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El libro '{self.__titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.__titulo}' no está disponible.")
    
    def devolver(self):
        self.__disponible = True
        print(f"El libro '{self.__titulo}' ha sido devuelto.")
    
    def __str__(self):
        disponibilidad = "Disponible" if self.__disponible else "No disponible"
        return f"Libro: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}, Estado: {disponibilidad}"
