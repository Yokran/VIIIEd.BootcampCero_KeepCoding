cadenaunidades = input("Cantidad: ")
cadenaprecio = input("precio unitario (€): ")
unidades = float(cadenaunidades)
precio = float(cadenaprecio)

totalItems = 0
precioTotal = 0

while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    print(precio, "€ -", unidades, "unidades-", totalUnitario, "€")
    
    totalItems += unidades #totalitems = totalitems + unidades
    precioTotal += precioUnitario
    
    cadenaunidades = input("Cantidad: ")
    cadenaprecio = input("precio unitario (€): ")
    unidades = float(cadenaunidades)
    precio = float(cadenaprecio)
    
print("--------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)
