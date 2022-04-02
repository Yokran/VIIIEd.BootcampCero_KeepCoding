strdolares = input("¿Cuántos dolares tienes? ")
strtasacambio = input("¿Cuál es la tasa de cambio? ")
dolares = float(strdolares)
tasacambio = float(strtasacambio)
euros = float(dolares) * float(tasacambio)

print("{} dolares a una tasa de cambio de {} Total {} €".format(dolares,tasacambio,euros))

#SOLUCIÓN:
strDolares = input("Dolares: ")
strTasa = input("Valor de cambio Dolar a Euro: ")

dolares = round(float(strDolares), 2)
tasa = float(strTasa)

euros = round(dolares * tasa, 2)

print("{} dolares a una tasa de intercambio {}\n{} €".format(dolares, tasa, euros))