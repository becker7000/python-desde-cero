import json
import os
from usuarios import Usuario, Cliente

RUTA_JSON = "usuarios.json"


def cargar_usuarios():
    """Carga todos los usuarios registrados desde el archivo JSON."""
    if not os.path.exists(RUTA_JSON):
        return []

    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    usuarios = []
    for item in datos:
        if "tarjeta16Digitos" in item:
            usuarios.append(Cliente.from_dict(item))
        else:
            usuarios.append(Usuario.from_dict(item))

    return usuarios


def guardar_usuarios(lista_usuarios):
    """Guarda la lista de objetos Usuario/Cliente en formato JSON."""
    datos = [u.to_dict() for u in lista_usuarios]

    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def registrar_usuario(usuario):
    """Agrega un nuevo usuario si el nickname no está registrado."""
    usuarios = cargar_usuarios()

    # Verificar nickname
    for u in usuarios:
        if u.nickname == usuario.nickname:
            return False   # nickname ya registrado

    usuarios.append(usuario)
    guardar_usuarios(usuarios)
    return True

class Cliente(Usuario):

    def __init__(self, nombre, apellido_paterno, apellido_materno, edad,
                 nickname, password, correo, celular,
                 tarjeta16Digitos):
        super().__init__(nombre, apellido_paterno, apellido_materno, edad,
                         nickname, password, correo, celular)
        self._tarjeta16Digitos = tarjeta16Digitos

    def to_dict(self):
        dic = super().to_dict()
        dic["tarjeta16Digitos"] = self._tarjeta16Digitos
        return dic

    @staticmethod
    def from_dict(dic):
        return Cliente(
            nombre=dic["nombre"],
            apellido_paterno=dic["apellido_paterno"],
            apellido_materno=dic["apellido_materno"],
            edad=dic["edad"],
            nickname=dic["nickname"],
            password=dic["password"],
            correo=dic["correo"],
            celular=dic["celular"],
            tarjeta16Digitos=dic["tarjeta16Digitos"]
        )

from admin_json import cargar_usuarios

def iniciar_sesion(nickname, password):
    usuarios = cargar_usuarios()

    for u in usuarios:
        if u.nickname == nickname and u.password == password:
            return u   # Inicio de sesión exitoso

    return None  # Datos incorrectos

from usuarios import Usuario, Cliente
from admin_json import registrar_usuario
from login import iniciar_sesion

# Registrar un usuario normal
u1 = Usuario(
    nombre="Juan",
    apellido_paterno="Pérez",
    apellido_materno="Lopez",
    edad=30,
    nickname="juan123",
    password="1234",
    correo="juan@mail.com",
    celular="555-123"
)

if registrar_usuario(u1):
    print("Usuario registrado correctamente.")
else:
    print("Error: el nickname ya existe.")


# Registrar un cliente
c1 = Cliente(
    nombre="Ana",
    apellido_paterno="Gomez",
    apellido_materno="Rios",
    edad=25,
    nickname="ana01",
    password="abcd",
    correo="ana@mail.com",
    celular="555-456",
    tarjeta16Digitos="1234123412341234"
)

registrar_usuario(c1)


# Probar login
nick = input("Ingrese su nickname: ")
pwd = input("Ingrese su contraseña: ")

usuario = iniciar_sesion(nick, pwd)

if usuario:
    print("Inicio de sesión exitoso.")
    print(f"Bienvenido {usuario.nombre}")

    if isinstance(usuario, Cliente):
        print("Menú de cliente...")
    else:
        print("Menú de usuario estándar...")
else:
    print("Nickname o contraseña incorrectos.")

"""
proyecto_usuarios/
│
├── main.py
├── admin_json.py
├── login.py
├── usuarios.json        ← se genera automáticamente
│
├── usuarios/
│   ├── __init__.py
│   ├── usuario.py
│   └── cliente.py
│
└── README.md

"""
