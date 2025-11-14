
listaestudiantes = []

def registrar_estudiantes ():
    estudiante = str(input("Nombre estudiante a registrar: ")).capitalize()
    edad = int(input("Edad del estudiante: "))
    listaestudiantes.append({"estudiante": estudiante,"edad": edad})
    print(f"Estudiante {estudiante} registrado correctamente.")

def promedio_notas():
    while True: 
        try:
            n1 = float(input("Ingrese nota1: "))
            n2 = float(input("Ingrese nota2: "))
            n3 = float(input("Ingrese nota3: "))
            if n1 and n2 and n3 < 0 or n1 and n2 and n3 > 5:
                print("Error: Las notas deben estar entre 0 y 5.")
                continue 
            promedio = (n1 + n2 + n3) / 3
            print(f"El promedio de las notas es: {promedio:.2f}")
            break
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido para las notas.")

def mostrar_estudiantes ():
    if len(listaestudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("Estudiantes registrados:")
        for estudiante in listaestudiantes:
            print(f"{estudiante}")


registrar_estudiantes()
promedio_notas()
mostrar_estudiantes()
