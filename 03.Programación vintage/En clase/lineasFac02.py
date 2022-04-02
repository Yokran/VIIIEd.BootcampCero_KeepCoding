cadenaunidades = input("Cantidad: ")
cadenaprecio = input("precio unitario (€): ")
unidades = float(cadenaunidades)
precio = float(cadenaprecio)

totalItems = 0
precioTotal = 0

cadenaImprimir = ""

while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    cadenaImprimir += str(precio) + "€ - " + str(unidades) + "unidades -" + str(totalUnitario) + "€\n"
#    cadenaImprimir += "{}€ - {} unidades - {}€\n".format(precio, unidades, totalUnitaio)
    totalItems += unidades #totalitems = totalitems + unidades
    precioTotal += totalUnitario
    
    cadenaunidades = input("Cantidad: ")
    cadenaprecio = input("precio unitario (€): ")
    unidades = float(cadenaunidades)
    precio = float(cadenaprecio)

print(cadenaImprimir)
print("--------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)
