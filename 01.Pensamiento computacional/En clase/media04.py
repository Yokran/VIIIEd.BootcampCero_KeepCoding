notas = (2, 4, 6, 8)

def contenido(lista, indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    return resultado


#Sumar notas

indice = 0
suma = 0
while contenido(notas, indice) !=None:
    suma = suma + notas[indice]
    indice = indice + 1
 
print("Numero de items; ", indice) 
print("Nota Total: ", suma)

#Calcular media
media = suma / indice

print("Nota Media: ", media)