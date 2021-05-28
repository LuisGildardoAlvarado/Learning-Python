print("proporciona los datos del libro:")
nombre = input("nombre del libro:")
Id = int(input("ID del libro:"))
precio = float(input("precio del libro:"))
enviogratuito = input("indica si el envio es gratuito (True/False):")

if enviogratuito == "True":
    enviogratuito = True
elif enviogratuito == "False":
    enviogratuito = False
else:
    enviogratuito = "valor incorrecto, debe ser True/False"
    
print("Nombre:", nombre)
print("ID:", Id)
print("precio:",precio)
print("envio gratuito:", enviogratuito)