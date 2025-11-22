# gestor_cine.py
# Migración simplificada del proyecto Java "gestor-cine" a Python
# Cada clase y función principal incluye comentarios explicativos (línea por línea o por bloque)

import json
import os
from dataclasses import dataclass, asdict
from typing import List, Optional

# -----------------------------
# Definición de la clase Usuario
# -----------------------------
@dataclass
class Usuario:
    # Atributos básicos de un usuario: nombre de usuario, contraseña y tipo
    username: str  # nombre de usuario (identificador)
    password: str  # contraseña en texto plano (nota: en producción usar hashing)
    tipo: str = "CLIENTE"  # tipo por defecto (CLIENTE, VENDEDOR, ADMIN)

    def to_dict(self) -> dict:
        # Convierte la instancia a diccionario (útil para almacenar en JSON)
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        # Crea una instancia de Usuario a partir de un diccionario
        return cls(username=data.get('username',''), password=data.get('password',''), tipo=data.get('tipo','CLIENTE'))

    def __str__(self) -> str:
        # Representación legible del usuario
        return f"Usuario(username={self.username}, tipo={self.tipo})"

# ---------------------------------
# Subclases: Administrador, Vendedor
# ---------------------------------
@dataclass
class Administrador(Usuario):
    # Administrador hereda de Usuario y cambia el tipo
    def __post_init__(self):
        # Asegura que el tipo esté marcado como ADMIN
        self.tipo = 'ADMIN'

    def __str__(self) -> str:
        # Representación especial para administrador
        return f"Administrador(username={self.username})"

@dataclass
class Vendedor(Usuario):
    # Vendedor hereda de Usuario y cambia el tipo
    def __post_init__(self):
        # Asegura que el tipo esté marcado como VENDEDOR
        self.tipo = 'VENDEDOR'

    def __str__(self) -> str:
        # Representación especial para vendedor
        return f"Vendedor(username={self.username})"

@dataclass
class Cliente(Usuario):
    # Cliente hereda de Usuario y mantiene tipo CLIENTE
    nombre: Optional[str] = None  # nombre real del cliente (opcional)

    def __post_init__(self):
        # Asegura que el tipo esté marcado como CLIENTE
        self.tipo = 'CLIENTE'

    def __str__(self) -> str:
        # Representación especial para cliente
        return f"Cliente(username={self.username}, nombre={self.nombre})"

# ---------------------------------
# Validaciones (equivalente a Validaciones.java)
# ---------------------------------
class Validaciones:
    """Clase estática con métodos de validación usados por los menús.
    Cada método es un pequeño wrapper que verifica condiciones comunes.
    """

    @staticmethod
    def es_usuario_valido(username: str) -> bool:
        # Verifica que el nombre de usuario tenga al menos 3 caracteres
        return isinstance(username, str) and len(username.strip()) >= 3

    @staticmethod
    def es_password_valida(password: str) -> bool:
        # Verifica que la contraseña tenga al menos 4 caracteres
        return isinstance(password, str) and len(password) >= 4

    @staticmethod
    def tipos_permitidos(tipo: str) -> bool:
        # Comprueba si el tipo de usuario es uno de los permitidos
        return tipo in ('ADMIN', 'VENDEDOR', 'CLIENTE')

# ---------------------------------
# GestorUsuarios: carga/guarda y operaciones
# ---------------------------------
class GestorUsuarios:
    # Archivo por defecto donde se guardan los usuarios (JSON)
    ARCHIVO = 'datos/usuarios.json'

    @classmethod
    def asegurar_directorio(cls):
        # Crea el directorio si no existe
        carpeta = os.path.dirname(cls.ARCHIVO)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta, exist_ok=True)

    @classmethod
    def cargar_usuarios(cls) -> List[Usuario]:
        # Carga la lista de usuarios del archivo JSON; devuelve lista vacía si no existe
        cls.asegurar_directorio()  # asegura que la carpeta exista
        if not os.path.exists(cls.ARCHIVO):
            # Si no existe el archivo, retorna lista vacía
            return []
        with open(cls.ARCHIVO, 'r', encoding='utf-8') as f:
            # Leer el JSON y convertir cada entrada a la clase correspondiente
            data = json.load(f)
        usuarios: List[Usuario] = []
        for entry in data:
            tipo = entry.get('tipo', 'CLIENTE')
            if tipo == 'ADMIN':
                usuarios.append(Administrador.from_dict(entry))
            elif tipo == 'VENDEDOR':
                usuarios.append(Vendedor.from_dict(entry))
            else:
                usuarios.append(Cliente.from_dict(entry))
        return usuarios

    @classmethod
    def guardar_usuarios(cls, usuarios: List[Usuario]):
        # Guarda la lista de usuarios en formato JSON
        cls.asegurar_directorio()  # asegura que la carpeta exista
        with open(cls.ARCHIVO, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in usuarios], f, ensure_ascii=False, indent=2)

    @classmethod
    def buscar_usuario(cls, username: str) -> Optional[Usuario]:
        # Busca un usuario por nombre de usuario y devuelve la instancia o None
        usuarios = cls.cargar_usuarios()
        for u in usuarios:
            if u.username == username:
                return u
        return None

    @classmethod
    def registrar_usuario(cls, usuario: Usuario) -> bool:
        # Registra un usuario si no existe ya; devuelve True si se registró
        usuarios = cls.cargar_usuarios()
        if any(u.username == usuario.username for u in usuarios):
            return False  # ya existe
        usuarios.append(usuario)
        cls.guardar_usuarios(usuarios)
        return True

    @classmethod
    def autenticar(cls, username: str, password: str) -> Optional[Usuario]:
        # Autentica las credenciales y devuelve el usuario si coinciden
        u = cls.buscar_usuario(username)
        if u and u.password == password:
            return u
        return None

    @classmethod
    def listar_usuarios(cls) -> List[Usuario]:
        # Devuelve la lista completa de usuarios
        return cls.cargar_usuarios()

# -----------------------------
# Menús (equivalente a los Menus en Java)
# -----------------------------

def menu_login() -> Optional[Usuario]:
    # Menú de login por consola: pide usuario y contraseña
    print('\n--- LOGIN ---')  # título del menú
    username = input('Usuario: ').strip()  # pide nombre de usuario
    password = input('Contraseña: ').strip()  # pide contraseña
    if not Validaciones.es_usuario_valido(username):
        print('Nombre de usuario inválido. Debe tener al menos 3 caracteres.')
        return None
    if not Validaciones.es_password_valida(password):
        print('Contraseña inválida. Debe tener al menos 4 caracteres.')
        return None
    user = GestorUsuarios.autenticar(username, password)  # intenta autenticar
    if user:
        print(f'Bienvenido {user.username} (tipo: {user.tipo})')
        return user
    else:
        print('Usuario o contraseña incorrectos.')
        return None


def menu_registro():
    # Menú para registrar usuarios nuevos
    print('\n--- REGISTRO ---')
    username = input('Nuevo usuario: ').strip()
    if not Validaciones.es_usuario_valido(username):
        print('Nombre de usuario inválido. Debe tener al menos 3 caracteres.')
        return
    if GestorUsuarios.buscar_usuario(username):
        print('El usuario ya existe. Elige otro nombre.')
        return
    password = input('Contraseña: ').strip()
    if not Validaciones.es_password_valida(password):
        print('Contraseña inválida. Debe tener al menos 4 caracteres.')
        return
    tipo = input('Tipo (ADMIN/VENDEDOR/CLIENTE) [CLIENTE]: ').strip().upper() or 'CLIENTE'
    if not Validaciones.tipos_permitidos(tipo):
        print('Tipo no permitido. Se usará CLIENTE por defecto.')
        tipo = 'CLIENTE'
    # Crear la instancia correcta según el tipo
    if tipo == 'ADMIN':
        nuevo = Administrador(username=username, password=password)
    elif tipo == 'VENDEDOR':
        nuevo = Vendedor(username=username, password=password)
    else:
        nombre_real = input('Nombre real (opcional): ').strip()
        nuevo = Cliente(username=username, password=password, nombre=nombre_real)
    ok = GestorUsuarios.registrar_usuario(nuevo)
    if ok:
        print('Usuario registrado con éxito.')
    else:
        print('No se pudo registrar el usuario (ya existe?).')


def menu_principal(usuario: Usuario):
    # Menú principal que muestra opciones según el tipo de usuario
    print('\n--- MENÚ PRINCIPAL ---')
    print(f'Usuario actual: {usuario.username} ({usuario.tipo})')
    if usuario.tipo == 'ADMIN':
        print('1) Listar usuarios')
        print('2) Registrar usuario')
        print('0) Salir')
        opcion = input('Selecciona una opción: ').strip()
        if opcion == '1':
            usuarios = GestorUsuarios.listar_usuarios()
            print('\n-- LISTADO USUARIOS --')
            for u in usuarios:
                print(u)
        elif opcion == '2':
            menu_registro()
        elif opcion == '0':
            print('Saliendo...')
        else:
            print('Opción no válida.')
    elif usuario.tipo == 'VENDEDOR':
        print('1) Ver perfil')
        print('0) Salir')
        opcion = input('Selecciona una opción: ').strip()
        if opcion == '1':
            print(usuario)
        elif opcion == '0':
            print('Saliendo...')
        else:
            print('Opción no válida.')
    else:  # CLIENTE
        print('1) Ver perfil')
        print('2) Registrarse como cliente (modificar perfil)')
        print('0) Salir')
        opcion = input('Selecciona una opción: ').strip()
        if opcion == '1':
            print(usuario)
        elif opcion == '2':
            print('Funcionalidad de edición de perfil no implementada (demo).')
        elif opcion == '0':
            print('Saliendo...')
        else:
            print('Opción no válida.')

# -----------------------------
# Punto de entrada simplificado
# -----------------------------

def main():
    # Bucle principal de la aplicación: permite login, registro y uso del menú principal
    print('Bienvenido al Gestor de Cine (versión migrada a Python)')
    while True:
        print('\n1) Iniciar sesión')
        print('2) Registrarse')
        print('0) Salir')
        opcion = input('Selecciona una opción: ').strip()
        if opcion == '1':
            user = menu_login()
            if user:
                menu_principal(user)
        elif opcion == '2':
            menu_registro()
        elif opcion == '0':
            print('Adiós.')
            break
        else:
            print('Opción no válida. Intenta de nuevo.')


if __name__ == '__main__':
    main()
