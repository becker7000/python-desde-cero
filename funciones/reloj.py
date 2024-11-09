import time
import os

def mostrar_reloj():
    while True:
        # Horario actual
        hora_actual = time.strftime("%H:%M:%S",time.localtime())
        # Limpiar la consola
        #if os.name == 'nt': # En el caso de windows
        os.system('cls')
        #else:
            #os.system('clear') # Linux o macOS
        # Mostramos el reloj:
        print(f" Hora actual: {hora_actual}")
        # Hacemos que el sistema se duerma 1 segundo:
        time.sleep(1)

if __name__ == "__main__":
    mostrar_reloj()

# Clean Code