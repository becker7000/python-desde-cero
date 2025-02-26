import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Clase Tarea para representar cada tarea individual
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion  # Descripción de la tarea
        self.fecha_agregado = datetime.now()  # Fecha y hora en que se creó la tarea
        self.realizada = False  # Estado de la tarea (si está realizada o no)

    # Método para marcar la tarea como realizada
    def marcar_como_realizada(self):
        self.realizada = True

    # Método para representar la tarea como string
    def __str__(self):
        return f"{self.descripcion} - {self.fecha_agregado.strftime('%Y-%m-%d %H:%M:%S')}"

# Clase ToDoList para manejar todas las tareas
class ToDoList:
    def __init__(self):
        self.tareas = []  # Lista de tareas

    # Método para agregar una nueva tarea a la lista
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    # Método para limpiar la lista de tareas
    def limpiar_lista(self):
        self.tareas.clear()

    # Método para obtener todas las tareas
    def obtener_tareas(self):
        return self.tareas

    # Método para marcar una tarea como realizada por índice
    def marcar_tarea_como_realizada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_como_realizada()

# Clase ToDoApp para la interfaz gráfica con Tkinter
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")  # Título de la ventana
        self.root.geometry("400x400")  # Tamaño fijo de la ventana 400x400 píxeles
        self.root.resizable(False, False)  # Desactiva el cambio de tamaño de la ventana
        self.todo_list = ToDoList()  # Creamos una instancia de ToDoList para gestionar las tareas

        # Etiqueta para indicar que se debe ingresar una nueva tarea
        self.label = tk.Label(self.root, text="Ingrese una nueva tarea:", font=("Arial", 12))
        self.label.pack(pady=5)

        # Campo de texto donde se escribe la nueva tarea
        self.tarea_input = tk.Entry(self.root, width=52)
        self.tarea_input.pack(pady=5)

        # Frame que contiene la lista de tareas y el scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Listbox para mostrar las tareas (la lista de tareas)
        self.tree = tk.Listbox(self.frame, width=50, height=10)
        self.tree.pack(side=tk.LEFT)

        # Scrollbar para desplazarse por la lista de tareas
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.config(yscrollcommand=self.scrollbar.set)

        # Botón para agregar una nueva tarea
        self.boton_agregar = tk.Button(self.root, text="Agregar Tarea", width=20, command=self.agregar_tarea, bg="#A7C7E7", relief="raised")
        self.boton_agregar.pack(pady=5)

        # Botón para limpiar la lista de tareas
        self.boton_limpiar = tk.Button(self.root, text="Limpiar Lista", width=20, command=self.limpiar_lista, bg="#A7C7E7", relief="raised")
        self.boton_limpiar.pack(pady=5)

        # Botón para marcar una tarea como realizada
        self.boton_marcar_realizada = tk.Button(self.root, text="Marcar como Realizada", width=20, command=self.marcar_realizada, bg="#A7C7E7", relief="raised")
        self.boton_marcar_realizada.pack(pady=5)

    # Método para actualizar la lista de tareas en la interfaz gráfica
    def actualizar_lista(self):
        self.tree.delete(0, tk.END)  # Limpiar la lista actual
        # Mostrar cada tarea con su estado y fecha de creación
        for idx, tarea in enumerate(self.todo_list.obtener_tareas()):
            estado = "Realizada" if tarea.realizada else "Pendiente"  # Verificar si la tarea está realizada
            # Insertar cada tarea en la lista con su descripción, estado y fecha
            self.tree.insert(tk.END, f"{idx + 1}. {tarea.descripcion} - {estado} - {tarea.fecha_agregado.strftime('%Y-%m-%d %H:%M:%S')}")

    # Método para agregar una tarea nueva
    def agregar_tarea(self):
        descripcion = self.tarea_input.get()  # Obtener la descripción de la tarea desde el campo de texto
        if descripcion.strip() != "":  # Verificar que la descripción no esté vacía
            nueva_tarea = Tarea(descripcion)  # Crear una nueva instancia de Tarea
            self.todo_list.agregar_tarea(nueva_tarea)  # Agregar la tarea a la lista
            self.tarea_input.delete(0, tk.END)  # Limpiar el campo de texto
            self.actualizar_lista()  # Actualizar la lista mostrada
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese una descripción para la tarea.")  # Advertencia si la tarea está vacía

    # Método para limpiar la lista de tareas
    def limpiar_lista(self):
        self.todo_list.limpiar_lista()  # Limpiar todas las tareas de la lista
        self.actualizar_lista()  # Actualizar la lista mostrada

    # Método para marcar una tarea como realizada
    def marcar_realizada(self):
        try:
            indice = int(self.tree.curselection()[0])  # Obtener el índice de la tarea seleccionada
            self.todo_list.marcar_tarea_como_realizada(indice)  # Marcar la tarea como realizada
            self.actualizar_lista()  # Actualizar la lista mostrada
        except IndexError:
            messagebox.showwarning("Selección inválida", "Por favor, selecciona una tarea para marcarla como realizada.")  # Advertencia si no se seleccionó ninguna tarea

# Función principal que crea la ventana y ejecuta la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = ToDoApp(root)  # Crear la instancia de la aplicación ToDoApp
    root.mainloop()  # Iniciar el ciclo de eventos de la ventana
