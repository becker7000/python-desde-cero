
from admin_json import cargar_usuarios

def iniciar_sesion(nickname,password):
    usuarios = cargar_usuarios()
    for usr in usuarios:
        if usr.nickname == nickname and usr.password == password:
            return usr # Se retorna el usuario (un usuario existente)
    return None