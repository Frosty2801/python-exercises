


def pedir_producto():
    nombre = input("Ingrese nombre del producto: ")
    if nombre: ""
    print("Nombre vacio: ")
    return nombre 
    
def pedir_precio():
    while True:
        precio = input("Ingrese precio del producto: ")
        if precio < 0:
            print("Error precio negativo")
        return precio
    
def pedir_cantidad():
    while True:
        cantidad = input("Ingrese la cantidad del producto: ")
        if cantidad <= 0: 
            print("Cantidad no puede ser negativa")
        else:
            return cantidad



nombre = pedir_producto()
precio = pedir_precio(float)
cantidad = pedir_cantidad(int)
