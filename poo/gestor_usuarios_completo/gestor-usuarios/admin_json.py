import json
import os
from usuarios import Usuario, Cliente

# To_do lo necesario para guardar o consumir el JSON

RUTA_JSON = "usuarios.json"

def cargar_usuarios():
    if not os.path.exists(RUTA_JSON):
        return [] # Retorno temprano, el mé_todo termina antes
    # r -> read
    with open(RUTA_JSON,"r",encoding="utf-8") as archivo_usuarios:
        datos = json.load(archivo_usuarios)

    # El JSON se tiene que guardar como una lista de diccionarios
    # donde cada diccionario es un usuario:
    usuarios = [] # Definimos la lista de usuarios vacía
    for usr in datos :
        if "tarjeta16Digitos" in usr:
            usuarios.append(Cliente.from_dict(usr))
        else:
            usuarios.append(Usuario.from_dict(usr))

    return usuarios


def guardar_usuarios(lista_usuarios):
    # Para cada usuario (de la lista_usuarios)
    # llamado usuario (nombre local al for)
    # crear un diccionario y guardarlo en datos
    datos = [ usuario.to_dict() for usuario in lista_usuarios ]

    # w -> write
    with open(RUTA_JSON,"w",encoding="utf-8") as archivo_usuarios:
        json.dump(datos,archivo_usuarios,indent=4,ensure_ascii=False)

def registrar_usuario(usuario):
    usuarios = cargar_usuarios()
    # Verificamos que el nickname no exista:
    for usr in usuarios:
        if usr.nickname == usuario.nickname:
            return False # El mé_todo termina sin guardar al usuario
    usuarios.append(usuario)
    guardar_usuarios(usuarios)
    return True # Cuando to_do sale bien...

