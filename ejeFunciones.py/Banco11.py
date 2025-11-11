
totalAhorro = 0

for mes in range(1,7):
    ahorro = float(input(f"Ingrese la cantidad {mes}: "))
    totalAhorro += ahorro
    
    if totalAhorro > 1000000:
        print(f"total acumulado: {totalAhorro}")
    else:
        print(f"meta alcanzada: {totalAhorro}")
