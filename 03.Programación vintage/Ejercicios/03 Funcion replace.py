'''
cadenaOriginal = input("Introduzca cadena: ")

cadenaOriginal = len(cadenaOriginal)

posicionMod = input("Introduzca posición a modifica: ")


valorMod = input("Introduzca valor de modificación: ")

for posicionMod in cadenaOriginal:
  cadenaOriginal = cadenaOriginal.remove(posicionMod)
  cadenaOriginal = cadenaOriginal.append(valorMod)

print(cadenaOriginal)
'''

def myReplace(cadena, posicion, nuevoValor):
  indice = 0
  resultado = ""
  while indice < len(cadena):
    if indice == posicion:
      resultado += nuevoValor
    else:
      resultado += cadena[indice]
      
    indice += 1

  return resultado