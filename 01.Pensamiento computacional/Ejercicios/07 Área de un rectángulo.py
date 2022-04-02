strancho = input("¿Cuánto mide la habitación de ancho? ")
strlargo = input("¿Y de largo? ")

ancho = float(strancho)
largo = float(strlargo)

superficie = ancho * largo
yardas = superficie / 0.91**2

print(superficie, "metros cuadrados")
print(yardas, "yardas")

#SOLUCIÓN
strLon = input("¿Longitud de la habitación en metros? ")
strProf = input("¿Profundo de la habitación en metros? ")

lon = float(strLon)
prof = float(strProf)

superficie = lon * prof
superficieYardas = superficie / 0.91**2

print("Superficie de la habitación en metros cuadrados: {}".format(superficie))
print("Superficie de la habitación en yardas cuadradss: {}".format(superficieYardas))
