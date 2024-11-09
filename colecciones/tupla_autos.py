
autos = []

# Marca, Modelo, Año
autos.append(("Toyota","Corolla",2019))
autos.append(("Honda","Civic",2014))
autos.append(("Subaru","WRX",2020))
autos.append(("Chevrolette","Malibu",2010))

print("Lista de automoviles: ")
for marca,modelo,anio in autos:
    print(f" >>> Marca: {marca}, modelo: {modelo}, Año: {anio}")
