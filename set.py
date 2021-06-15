#set
planetas ={"Mercurio", "Venus", "Tierra"}
print(planetas)

#largo
print(len(planetas))

#revisar si un elemento esta presente
print("Marte" in planetas)

#agregar un elemento
planetas.add("Marte")
print(planetas)

#eliminar elemento (con posible error)
planetas.remove("Mercurio")
print(planetas)

#eliminar elemento (sin error)
planetas.discard("Tierra")
print(planetas)

#limpiar set
planetas.clear()
print(planetas)

#eliminar el set
del planetas
print(planetas)
