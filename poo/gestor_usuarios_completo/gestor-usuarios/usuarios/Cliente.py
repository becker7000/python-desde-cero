from usuarios.Usuario import Usuario

class Cliente(Usuario):

    def __init__(
            self,
            nombre: str,
            apellido_paterno: str,
            apellido_materno: str,
            edad: int,
            nickname: str,
            password: str,
            correo: str,
            celular: str,
            tarjeta16Digitos: str
    ):
        super().__init__(
            nombre,
            apellido_paterno,
            apellido_materno,
            edad,
            nickname,
            password,
            correo,
            celular
        )
        self._tarjeta16Digitos = tarjeta16Digitos

    def to_dict(self):
        diccionario = super().to_dict()
        diccionario["tarjeta16Digitos"] = self._tarjeta16Digitos
        return diccionario

    @staticmethod
    def from_dict(diccionario):
        return Cliente(
            nombre = diccionario["nombre"],
            apellido_paterno = diccionario["apellido_paterno"],
            apellido_materno = diccionario["apellido_materno"],
            edad = diccionario["edad"],
            nickname = diccionario["nickname"],
            password = diccionario["password"],
            correo = diccionario["correo"],
            celular = diccionario["celular"],
            tarjeta16Digitos = diccionario["tarjeta16Digitos"]
        )
