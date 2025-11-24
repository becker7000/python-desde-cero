
from usuarios.Usuario import Usuario
from usuarios.Cliente import Cliente
from admin_json import registrar_usuario, cargar_usuarios
from login import iniciar_sesion

# Prueba 1 -> Lista vacía:
# print("\n\t Usuarios existentes: ")
# print(cargar_usuarios())

# Prueba 2 -> Guardando un usuario:
usuario1 = Usuario(
    nombre="Laura",
    apellido_paterno="Lopez",
    apellido_materno="Jimenez",
    edad=22,
    nickname="lau22lop",
    password="1234",
    correo="lau22lop@fakemail.com",
    celular="5512345678"
)

# Tenemos 2 opciones, que el usuario se pueda registrar o que ya existe:
if registrar_usuario(usuario1):
    print("\n\t USUARIO REGISTRADO CORRECTAMENTE")
else:
    print("\n\t ERROR: EL NICKNAME YA EXISTE, NO SE PUEDE VOLVER A REGISTRAR")