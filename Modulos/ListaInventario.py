
listainventario = []

def agregar_producto ():
    print("AGREGAR PRODUCTO")
nombre = (input("producto a añadir: "))


while True:
    try:
        pedir_precio = input("Ingrese el precio del producto: ")
        precio = float(pedir_precio)

        if precio < 0:
            print("Error precio negativo. Intentelo de nuevo.")
            continue
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio: ")

while True: 
    try: 
        pedir_cantidad = input("Ingresa cantidad del producto: ")
        cantidad = int(pedir_cantidad)
        if cantidad < 0:
            print("Error cantidad negativa")
            continue
        break
    except ValueError:
        print ("Error cantidad invalida, intente nuevamente: ")

producto = {
        'nombre' : nombre,
        "precio" : precio,
        "cantidad" : cantidad
}
listainventario.append(producto)
print(f"producto {nombre} agregado")


def mostrar_inventario():
    for lista in range(listainventario):
        if lista == "":
            print("La lista esta vacia")
        else: 
            print(f"{listainventario}")
        return






