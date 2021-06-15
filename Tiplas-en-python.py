#Definir una tupla
frutas = ("Naranja","platano", "guayaba")

#saber el largo
print(len(frutas))

#acceder a un elemento
print (frutas[0])

#navegacion inversa
print(frutas[-2])

#acceder a un rango
print(frutas[0:1]) #sin incluir el ultimo indice

#recorrer elementos
for fruta in frutas:
    print(fruta, end=" ")
    
#cambiar valor a tupla
#frutas[0] = "pera"
            #Tupla a lista
frutalista = list(frutas)
frutalista[0] = "pera"
frutas = tuple(frutalista)

print('\n',frutas)

#eliminar tupla
del (frutas)
print(frutas)


    