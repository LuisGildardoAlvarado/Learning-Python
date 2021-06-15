# definir una lista de tipo str
nombres = ["Jaime","Jordi","Keila","Marco"]

# imprimir lista de nombres
print(nombres)

#acceder a elementos de una lista
print(nombres[0])
print(nombres[2])

# acceder a elementos de una lista de manera inversa
print(nombres[-1])

#imprimir un rango
print(nombres[0:2])# sin inlcuir el indice 2

#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])

#desde el indice indicado hasta el final
print(nombres[1:])

#cambiar un valor
nombres[3] = "Abigail"
print(nombres)

#iterar un lista
for nombre in nombres:
    print(nombre)
else:
    print("no existen mas nombres en la lista")
    
#preguntar el largo de una lista
print(len(nombres)) 

#agregar un elemento a la lista
nombres.append("Lorenzo") 
print(nombres)

#agregar un elemento en un indice en especifico
nombres.insert(0, "David")
print(nombres)

#remover un elemento
nombres.remove("Jordi")
print (nombres)

#remover el ultimo valor agregado
nombres.pop()
print(nombres)

#eliminar un indice
del nombres[0]
print(nombres)

#limpiar la lista
nombres.clear()
print(nombres)

#borrar la lista por completo
del nombres
print(nombres)
