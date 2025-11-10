


horas = float(input("Ingrese cantidad de horas: "))

tarifa = 2000 * horas
multa = 2000 * horas + 5000

if horas < 0: 
    print("Horas invalidas")

elif horas >= 0 and horas < 5:
    print(f"Total a pagar: {tarifa}")

elif horas == 5: 
    print(f"Total a pagar: {multa}")

else:
    print("Horas totales: ")




