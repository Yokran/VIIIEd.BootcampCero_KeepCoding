strAnno1 = input("¿Cuántos años tienes? ")
strAnno2 = input("¿A que edad te jubilaras? ")
Anno1 = int(strAnno1)
Anno2 = int(strAnno2)

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
anno = date.strftime("%Y")

edadjubilacion = int(Anno2) - int(Anno1)
jubilacion = int(anno) + int(Anno2) - int(Anno1)

print("Te quedan", edadjubilacion, "años para jubilarte.")
print("Estamos en,", anno, "te jubilarás en", jubilacion,".")

#SOLUCIÓN
import datetime

ahora = datetime.datetime.now()
año = ahora.year

strEdad = input("¿Cuantos años tienes? ")
strJubilacion = input("¿A qué edad quieres jubilarte? ")

edad = int(strEdad)
jubilacion = int(strJubilacion)

faltan = jubilacion - edad
cuando = año + faltan

print("Te quedan {} años para jubilarte".format(faltan))

print("Estamos en {}, te jubilarás en {}".format(año, cuando))