

def calcular_propina ():
    cuenta = (int(input("Ingreses el total de la cuenta: ")))
    
    if cuenta >= 100000:
        propina = cuenta * 0.10
    else: 
        propina = cuenta * 0.15

    total_final = cuenta - propina 

    print(f"Total cuenta {total_final}")

calcular_propina()


