condicion = True
if condicion == True:
    print("la condicion es verdadera")
elif condicion == False:
    print("la condicion es falsa")
else:
    print("condicion no reconocida")

numero = int(input("proporciona un numero entre 1 y 3:"))
if numero == 1:
    numerotexto = "numero uno"
elif numero == 2:
    numerotexto = "numero dos"
elif numero == 3:
    numerotexto = "numero tres"
else:
    numerotexto = "numero fuera de rango"
    
print("numero proporcionado:", numerotexto)
