tasalitros = 0.05

strLon = input("Ancho del techo: ")
strProf = input("Profundo del techo: ")

lon = float(strLon)
prof = float(strProf)

area = lon * prof

litros = area * tasalitros
botes = litros // 5

botes += 1 if litros % 5 > 0 else 0

print("Necesitarás {} litros para pintar {} metros cuadrados de techo.".format(round(litros,2), round(area, 2)))
print("Debes comprar {} botes de pintura".format(botes))

#SOLUCIÓN
tasalitros = 0.05

strLon = input("Ancho del techo: ")
strProf = input("Profundo del techo: ")

lon = float(strLon)
prof = float(strProf)

area = lon * prof

litros = area * tasalitros
botes = litros // 5

botes += 1 if litros % 5 > 0 else 0

print("Necesitarás {} litros para pintar {} metros cuadrados de techo.".format(round(litros,2), round(area, 2)))
print("Debes comprar {} botes de pintura".format(botes))