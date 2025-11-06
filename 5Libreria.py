

libro = 25000
descuento = 0.15
cupon = 0.10

estudiante = input("Es usted estudiante?: (si / no) ").lower
regalo = ("Tienes algun tajeta de regalo? ingresalo (o deja vacio): ").upper


if estudiante == "si":
    Ldescuento = (libro * descuento)- descuento
    print("precio del libro con descuento (10%)  ")

else:
    print(f"precio completo: {libro}")

    if regalo == "LIBRO10":
        total = libro * 0.10
        print("Cupon valido adicional (10%): ")

    elif regalo != "":
        print("Cupon invalido ")

    elif not estudiante and regalo: 
        total = libro
        print("Precio completo: ")
 








