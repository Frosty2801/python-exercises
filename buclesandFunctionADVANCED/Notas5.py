

def promedio_notas():
    while True: 
        try:
            n1 = float(input("Ingrese nota1: "))
            n2 = float(input("Ingrese nota2: "))
            n3 = float(input("Ingrese nota3: "))
        except ValueError:
            print("Numero invalido")
            continue

        promedio = (n1, n2, n3) / 3
        if promedio >= 3.0:
            print(f"Aprobado {promedio}")
        else:
            print(f"Reprobado {promedio}")
        break

promedio_notas()


