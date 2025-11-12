

def evaluar_creditos():
    ingresos = float(input("Ingrese sus ingresos: "))
    edad = int(input("ingrese su edad: "))
    
    if ingresos > 2000000 and edad >= 25 and edad <= 60:
        print("credito aprobado")
    else:
        print("Credito rechazado")
    
evaluar_creditos()


