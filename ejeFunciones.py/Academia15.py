
estudiante = int(input("Ingrese el numero: "))

for i in range(1, estudiante + 1):
    if i % 5 == 0:
        print("Gran avance")
    else:
        print(f"ejercisio {i} completado")

