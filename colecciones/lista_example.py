
# Las listas son homegeneas y son mutables:
personas = ["Laura","Pedro","Luis","Ana","Ulises","Julia","Naomi"]

print(personas)

# Un elemento que llegará después:
personas.append("Carlos")

# Eliminando un elemento:
personas.remove("Luis")

# Colocando un elemento en un índice especifico:
personas.insert(3,"Lucia")

print("Lista de personas: ")
for p in personas:
    print(f"-> {p}")

print(f" Persona en el índice 2: {personas[2]}")