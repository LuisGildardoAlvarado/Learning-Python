a = int(input("proporciona un valor:"))

valorminimo=0
valormaximo=5
#and:
dentrorango= a>=valorminimo and a<=valormaximo
#print(dentrorango)
if(dentrorango):
    print("dentro de rango")
else:
    print("fuera de rango")

#or: 
vacaciones = False
diadescanso = False
if(vacaciones or diadescanso):
    print("puedes ir al parque")
else:
    print("te la jalas todo el dia")

#not:
print(not(vacaciones))
