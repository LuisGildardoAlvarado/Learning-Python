#dict   key :  value
diccionario = {
    "IDE":"Integrated Development Enviroment",
    "OOP":"Object Oriented Programming",
    "DMS":"Database Management System"
}
print(diccionario)

#largo(cantidad de elementos)
print(len(diccionario))

#aaceder a un elemento (key)
print(diccionario["IDE"])

#otra forma de recuperar un elemento
print(diccionario.get("OOP"))

#modificar elementos
diccionario["IDE"]= "integrated development enviroment"
print(diccionario)

#recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)
    
for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#comprobar existencia de algun elemento
print("IDE"in diccionario)

#Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

#remover un elemento
diccionario.pop("DMS")
print(diccionario)

#limpiar
diccionario.clear()
print(diccionario)

#eliminar el diccionario
del diccionario
