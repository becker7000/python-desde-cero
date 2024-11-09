import os

# Función para mostrar un menú:
def mostrar_menu():
    print("\n\t +-------------MENÚ------------+")
    print("\t | 1. Agregar una tarea        |")
    print("\t | 2. Ver todas las tareas      |")
    print("\t | 3. Eliminar tarea           |")
    print("\t | 4. Salir                    |")
    print("\t +-----------------------------+")

# Para cambiar la forma de insersión
# del teclado usamos: insert (ins) o alt+shift

def agregar_tarea(tareas):
    tarea = input("Escribre una tarea: ")
    if tarea:
        tareas.append(tarea)
        print("Tarea guarda correctamente")
    else:
        print("La tarea no debe ser vacía")

def ver_tareas(tareas):
    if len(tareas)==0:
        print("No tienes tareas pendientes en la lista")
    else:
        print("\n Lista de tareas: ")
        for i, tarea in enumerate(tareas,1):
            print(f" {i}. {tarea}")

def main():
    tareas = []
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Escribe tu opción: "))
            if opcion==1:
                agregar_tarea(tareas)
            elif opcion==2:
                ver_tareas(tareas)
            elif opcion==3:
                print("Eliminando tarea")
                # TODO: implementar una función para eliminar
            elif opcion==4:
                print("Hasta luego, todas tareas se borraran")
                break
            else:
                print("Opción no válida en el menú")
        except ValueError:
            print("Por favor, ingresa una opción entre 1 y 4")

# Ejecutar el programa:
if __name__ == "__main__":
    main()