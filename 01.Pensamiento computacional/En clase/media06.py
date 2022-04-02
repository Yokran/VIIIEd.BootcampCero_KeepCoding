notas = (2, 4, 6, 8)

#Calcular media
indice = 0
suma = 0
while indice < len(notas):
    suma = suma + notas[indice]
    indice = indice + 1
 
#Presentar media
media = suma / indice

print("Numero de items; ", indice) 
print("Nota Total.....: ", suma)
print("Nota Media.....: ", media)
