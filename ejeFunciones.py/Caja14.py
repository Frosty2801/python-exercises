total_vendido = 0

while True:
    monto = float(input("Ingrese el monto de la venta (0 para terminar): "))

    if monto == 0:
        break

    if monto >= 100000:
        print("¡Venta destacada!")

    total_vendido += monto

print(f"Total vendido: ${total_vendido:,.2f}")

