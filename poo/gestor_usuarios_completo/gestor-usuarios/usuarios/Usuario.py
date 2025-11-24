
class Usuario:

    # Contructor:
    def __init__(
            self,
            nombre: str,
            apellido_paterno: str,
            apellido_materno: str,
            edad: int,
            nickname: str,
            password: str,
            correo: str,
            celular: str
    ):
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._edad = edad
        self._nickname = nickname
        self._password = password
        self._correo = correo
        self._celular = celular

    # Getters y setters:

    @property # Sirve para anotar un mé_todo como getter
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,val):
        self._nombre = val

    @property
    def apellido_paterno(self):
        return self._apellido_paterno

    @apellido_paterno.setter
    def apellido_paterno(self,val):
        self._apellido_paterno = val

    @property
    def apellido_materno(self):
        return self._apellido_materno

    @apellido_materno.setter
    def apellido_materno(self,val):
        self._apellido_materno = val

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,val):
        self._edad = val

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self,val):
        self._nickname = val

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,val):
        self._password = val

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self,val):
        self._correo = val

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self,val):
        self._celular = val

    # Transforma un objeto Python de la clase Usuario a diccionario
    # para guarda en el JSON
    def to_dict(self):
        diccionario = {
            "nombre": self._nombre,
            "apellido_paterno": self._apellido_paterno,
            "apellido_materno": self._apellido_materno,
            "edad": self._edad,
            "nickname": self._nickname,
            "password": self._password,
            "correo": self._correo,
            "celular": self._celular
        }
        return diccionario

    # Transforma un diccionario del JSON a un objeto Python de la clase Usuario
    # Este mé_todo entrega un objeto de la clase Usuario dado un diccionario
    @staticmethod # Se pueden usar sin necesidad de crear un objeto de la clase misma
    def from_dict(diccionario : dict):
        return Usuario(
            nombre = diccionario["nombre"],
            apellido_paterno = diccionario["apellido_paterno"],
            apellido_materno = diccionario["apellido_materno"],
            edad = diccionario["edad"],
            nickname = diccionario["nickname"],
            password = diccionario["password"],
            correo = diccionario["correo"],
            celular = diccionario["celular"]
        ) # Nota: existen librerias con métodos para
          # entregar diccionarios a partir de objetos y viceversa

    # Mé_todos especial, genera una cadena con los datos del usuario
    def __str__(self):
        return f"""
                    +-------------USUARIO-------------+
                    | Nombre: {self._nombre}
                    | Apellido paterno: {self._apellido_paterno}
                    | Apellido materno: {self._apellido_materno}
                    | Edad: {self._edad}
                    | Nickname: {self._nickname}
                    | Password: {self._password}
                    | Correo: {self._correo}
                    | Celular: {self._celular}
                    +----------------------------------+
                """

# Estudiar niveles de acceso en atributos y métodos de una clase
