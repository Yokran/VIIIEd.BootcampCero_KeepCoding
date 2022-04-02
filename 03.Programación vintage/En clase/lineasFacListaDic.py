cadenaunidades = input("Cantidad: ")
cadenaprecio = input("precio unitario (€): ")

unidades = float(cadenaunidades)
precio = float(cadenaprecio)

totalItems = 0
precioTotal = 0

listaLineasFact = []

while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    item = dict()
    item ["unidades"] = unidades
    item ["precio"] = precio
    
    listaLineasFact.append(item)
    
    precioTotal += totalUnitario
    
    cadenaunidades = input("Cantidad: ")
    cadenaprecio = input("precio unitario (€): ")
    unidades = float(cadenaunidades)
    precio = float(cadenaprecio)

for item in listaLineasFact:
    print(item["precio"], "€ -", item["unidades"], "unidades -", item["unidades"] * item["precio"], "€")

print("--------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)



