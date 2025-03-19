
class Contacto:

    # Constructor
    def __init__(self,id_contacto,nombre,telefono,correo):
        self.id_contacto = id_contacto
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    # Mé_todo string (entrega una cadena de datos)
    def __str__(self):
        return f"==> {self.id_contacto} - {self.nombre} - {self.telefono} - {self.correo}"

# pyscript (version fuertemente tipada de Python)
# typescript (version fuertemente tipada de Java)
# java (es fuertemente tipado y usa var para ser debilmente tipado)

class Agenda:

    def __init__(self):
        self.contactos = []

    def agregar_contacto(self,contacto_nuevo):
        # Verificamos si ya existe el id: (evitamos duplicados)
        for contacto in self.contactos:
            if contacto.id_contacto == contacto_nuevo.id_contacto:
                print(f"\nYa existe un contacto con el id {contacto_nuevo.id_contacto}")
                return # Termina el mé_todo
        self.contactos.append(contacto_nuevo)
        print(f"Contacto con id {contacto_nuevo.id_contacto} agregado correctamente")

    def ver_contactos(self):
        # return [str(contacto) for contacto in self.contactos]
        if self.contactos:
            print("\nLista de contactos:")
            for contacto in self.contactos:
                print(contacto)
        else:
            print("La agenda está vacía...")

    def editar_contacto(self,id_contacto, nuevo_nombre=None, nuevo_telefono=None, nuevo_correo=None):
        # None significa que un parametro puede ser ausente
        for contacto in self.contactos:
            if contacto.id_contacto == id_contacto: # Buscamos por id
                if nuevo_nombre: # Ejemplo con1.editar_contacto(4,nuevo_telefono="55102938347")
                    contacto.nombre = nuevo_nombre
                    print("Se ha editado el nombre del contacto")
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono
                    print("Se ha editado el telefono del contacto")
                if nuevo_correo:
                    contacto.correo = nuevo_correo
                    print("Se ha editado el correo del contacto")
                print(f"El contacto con el id {id_contacto} fue modificado correctamente")
                return # Termina la función editar_contacto
        print(f"No existe un contacto con el id {id_contacto}")

    def eliminar_contacto(self,id_contacto):
        for contacto in self.contactos:
            if contacto.id_contacto == id_contacto:
                self.contactos.remove(contacto)
                print(f"El contacto con el id {id_contacto} "
                      f"de nombre {contacto.nombre} se elimino correctamente")
                return # Termina el mé_todo eliminar_contacto
        print(f"No existe un contacto con el id {id_contacto}")

    def buscar_por_id(self,id_contacto):
        for contacto in self.contactos:
            if contacto.id_contacto == id_contacto:
                print("Contacto encontrado")
                print(contacto)
                return # Fin del mé_todo
        print(f"No existe un contacto con el id {id_contacto}")

    def limpiar_agenda(self):
        # TODO: Crear el código para eliminar todos los contactos
        pass # significa que en el futuro será implementado su código

# Las clase se nombran con PascalCase (ClientePlus)
# Los métodos se nombran con snake case: (agregar_contacto, ver_contactos)
