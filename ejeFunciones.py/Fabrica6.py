

productos = int(input("Ingrese cantidad de productos: "))

for i in range(1, productos):
    if i % 2 == 0:
        print(f"es par {i}")
    else:
        print(f"es impar {i}")

