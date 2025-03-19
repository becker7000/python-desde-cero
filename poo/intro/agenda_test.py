from contacto import Contacto,Agenda

# Creando una agenda vacía
agenda = Agenda()

# Mé_todo personalizado
agenda.ver_contactos()

# Creamos algunos contactos:
con1 = Contacto(1,"Juan","5512345678","juan_100@gmail.com")
con2 = Contacto(2,"Laura","5598765432","lau22_ram@gmail.com")

# Agregamos los contactos a la agenda:
agenda.agregar_contacto(con1)
agenda.agregar_contacto(con2)

# Volvemos a visualizar la agenda:
agenda.ver_contactos()

# Editando un contacto
print("\nEditando un contacto")
agenda.editar_contacto(2,nuevo_telefono="7701928374",nuevo_correo="laura_34_lopez@gmail.com")

# Volvemos a ver la lista:
agenda.ver_contactos()

# Buscando un contacto por id:
print("\nBuscando un contacto")
agenda.buscar_por_id(1)
agenda.buscar_por_id(8) # Este contacto no exite aún

# Eliminando un contacto por id:
print("\nEliminando un contacto")
agenda.eliminar_contacto(1)

# Volvemos a ver la lista:
agenda.ver_contactos()

# Agregamos un contacto duplicando un id
con3 = Contacto(2,"Eder","5612340088","eder_07_san@gmail.com")
agenda.agregar_contacto(con3)

# Volvemos a ver la lista:
agenda.ver_contactos()