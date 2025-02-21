# main.py
from biblioteca import Biblioteca
from libro import Libro
from miembro import Miembro

# Crear objetos de libro, miembro y biblioteca
libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", "9780743273565")
libro2 = Libro("1984", "George Orwell", "9780451524935")
miembro1 = Miembro("Juan Pérez", 25, "M001")
miembro2 = Miembro("Ana Gómez", 30, "M002")

# Crear la biblioteca y agregar libros y miembros
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_miembro(miembro1)
biblioteca.agregar_miembro(miembro2)

# Listar libros y miembros
biblioteca.listar_libros()
biblioteca.listar_miembros()

# Prestar y devolver libros
miembro1.prestar_libro(libro1)
miembro1.prestar_libro(libro2)
miembro1.devolver_libro(libro1)

# Ver estado de los libros después de las acciones
biblioteca.listar_libros()
