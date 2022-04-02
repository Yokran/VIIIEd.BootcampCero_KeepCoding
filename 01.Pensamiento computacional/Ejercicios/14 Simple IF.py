strprecio = input("Precio del producto: ")
provincia = input("Introduzca la provincia de residencia:")


subtotal = int(strprecio)
tasa = subtotal * 5.5 / 100
total = subtotal + tasa

if provincia == "VA":
    print("El subtotal es {} €".format(subtotal))
    print("La tasa es {} €".format(tasa))
    print("El total es {} €".format(total))

else:
    print("El total es {} €".format(subtotal))

#SOLUCIÓN
strPrecio =    input("Precio...: ")
strProvincia = input("Provincia: ")

total = float(strPrecio)
strTotal = ""

if strProvincia == 'VA':
  tasa = total * 0.055
  strTotal = "El subtotal es {:.2f}€\nLa tasa es {:.2f}€\n".format(total, tasa)
  total = total + tasa

strTotal = strTotal + "El total es {:.2f}€".format(total)
print(strTotal)