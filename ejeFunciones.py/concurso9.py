import random


numRandom = random.randint(1,6)
print(f"tienes {numRandom}, oportunidades")


for i in range(numRandom):
    secreto= ""
    secreto = int(input("ingresar un numero del 1 al 6 y adivina cual es:  "))
    if numRandom != secreto:
        print("es incorrecto")
    else:
        print("el numero es correcto", numRandom)
        break

