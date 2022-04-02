strprecio1 = input("Precio del producto 1: ")
strprecio2 = input("Precio del producto 2: ")
strprecio3 = input("Precio del producto 3: ")

strproducto1 = input("Número de ejemplares del producto 1: ")
strproducto2 = input("Número de ejemplares del producto 2: ")
strproducto3 = input("Número de ejemplares del producto 3: ")

precio1 = int(strprecio1)
precio2 = int(strprecio2)
precio3 = int(strprecio3)

producto1 = int(strproducto1)
producto2 = int(strproducto2)
producto3 = int(strproducto3)

subtotal = (precio1 * producto1) + (precio2 * producto2) + (precio3 * producto3)
tasa = subtotal * 5.5 / 100
total = subtotal + tasa

print("Subtotal: ",subtotal,"Tasas: ",tasa,"Total: ",total)

#SOLUCIÓN:
strPrice01 = input("Precio 01: ")
strQ01 = input("Cantidad 01: ")

strPrice02 = input("Precio 02: ")
strQ02 = input("Cantidad 02: ")

strPrice03 = input("Precio 03: ")
strQ03 = input("Cantidad 03: ")

price01 = float(strPrice01)
Q01 = float(strQ01)
price02 = float(strPrice02)
Q02 = float(strQ02)
price03 = float(strPrice03)
Q03 = float(strQ03)

subtotal = 0
subtotal += price01*Q01
subtotal += price02*Q02
subtotal += price03*Q03

tax = subtotal * 5.5

total = subtotal + tax

print("Subtotal: {}".format(subtotal))
print("Tasas: {}".format(tax))
print("Total: {}".format(total))