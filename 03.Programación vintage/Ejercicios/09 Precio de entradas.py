entradaBebe = int(0)
entradaNino = int(14)
entradaJubilado = int(18)
entradaAdulto = int(23)

edad = input("Introduzca edad: ")

while edad != 0:
    if  edad > 0 and <= 2:
        entradaBebe += 0
    elif edad > 2 and edad <= 12:
        entradaNino += 14
    elif edad > 12 and edad < 65:
        entradaJubilado += 18
    else:
        entradaAdulto += 23

precioTotal = int(entradaBebe + entradaNino + entradaAdulto + entradaJubilado)

print("Entradas de baby (0€)........: ", entradaBebe)
print("Entradas de menores (0€).....: ", entradaNino)
print("Entradas de normales (0€)....: ", entradaAdulto)
print("Entradas de jubilado (0€)....: ", entradaJubilado)

print(precioTotal)


