cadenaunidades = input("Cantidad: ")
cadenaprecio = input("precio unitario (€): ")
unidades = float(cadenaunidades)
precio = float(cadenaprecio)

totalItems = 0
precioTotal = 0

listaPrecios = []
listaUnidades = []

while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    listaPrecios.append(precio)
    listaUnidades.append(unidades)
    
    precioTotal += totalUnitario
    
    cadenaunidades = input("Cantidad: ")
    cadenaprecio = input("precio unitario (€): ")
    unidades = float(cadenaunidades)
    precio = float(cadenaprecio)

indice = 0
while indice < len(listaPrecios):
    print(listaPrecios[indice], "€ -", listaUnidades[indice], "unidades -", listaPrecios[indice] * listaUnidades[indice], "€")
    indice += 1

print("--------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)

