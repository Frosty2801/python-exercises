

menu = 12000
bebida = 3000
subtotal = bebida + menu
iva = subtotal * 0.08

pedido = input("Menu con bebida (si / no): ")


if pedido == "si": 
    print(f"Su pedido con bebida {iva + subtotal}")

elif pedido == "no":
    print(f"Su pedido sin bebida {menu + iva}")


