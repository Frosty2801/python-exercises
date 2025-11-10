

libro = 25000
descuento = 0.15
cupon = 0.10
ESTdescuento = libro * descuento
totalDES = libro - ESTdescuento
regalo = descuento + cupon
CUPdescuento = libro * regalo
totalCUP = libro - CUPdescuento

estudiante = input("Es usted estudiante?: (si / no) ")
tarjeta = input("Tienes algun tajeta de regalo? ingresalo (o deja vacio): ")

if estudiante == "si":
    print(f"precio libro con descuento:{totalDES}")

elif estudiante == "no":
    print(f"precio completo:{libro} ")


if tarjeta == "LIBRO10":
    print(f"Cupon valido adicional: {totalCUP} ")

elif tarjeta != "LIBRO10":
    print(f"Cupon invalido: {libro} ")

elif not estudiante and tarjeta: 
    onlytarjeta = libro * cupon
    totalonly = libro - onlytarjeta
    print(f"Precio completo: {totalonly}")







