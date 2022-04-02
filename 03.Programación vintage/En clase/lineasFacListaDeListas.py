_UNIDADES = 1
_PRECIO = 0

cadenaunidades = input("Cantidad: ")
cadenaprecio = input("precio unitario (€): ")
unidades = float(cadenaunidades)
precio = float(cadenaprecio)

totalItems = 0
precioTotal = 0

listaLineasFact = []

while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    item = []
    item.append(unidades)
    item.append(precio)
    
    listaLineasFact.append(item)
    
    precioTotal += totalUnitario
    
    cadenaunidades = input("Cantidad: ")
    cadenaprecio = input("precio unitario (€): ")
    unidades = float(cadenaunidades)
    precio = float(cadenaprecio)

for item in listaLineasFact:
    print(item[_PRECIO], "€ -", item[_UNIDADES], "unidades -", item[_UNIDADES] * item[_PRECIO], "€")

print("--------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)


