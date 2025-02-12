# archivo_pass_funcion.py

# Definiendo una función que no hace nada
def funcion_vacia():
    pass  # Aquí no hacemos nada, solo se pasa sin ejecutar código

# Llamando a la función
funcion_vacia()

print("La función fue llamada, pero no hace nada.")


# archivo_continue_funcion.py

# Función que recorre una lista de números
def procesar_numeros():
    numeros = [10, 15, 0, -5, 20, 0, 30]
    
    for num in numeros:
        if num == 0:
            print("Número cero encontrado, continuando con el siguiente número.")
            continue  # Si el número es 0, saltamos a la siguiente iteración del bucle
        print(f"Procesando el número: {num}")

# Llamamos a la función
procesar_numeros()

# archivo_break_funcion.py

# Función que recorre una lista de números
def buscar_numero():
    numeros = [10, 15, 0, -5, 20, 25, 30]
    
    for num in numeros:
        if num == 20:
            print("Número 20 encontrado. Rompiendo el bucle.")
            break  # Si encontramos el número 20, salimos del bucle
        print(f"Procesando el número: {num}")

# Llamamos a la función
buscar_numero()

