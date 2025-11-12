
def repeticiones():
    NUMrepeticiones = (int(input("Numero de repeticiones: ")))

    for numero in range(1, NUMrepeticiones):

        if numero % 2 == 0:
            print("Excelente forma")
        else: 
            print("Manten el ritmo")

repeticiones()

