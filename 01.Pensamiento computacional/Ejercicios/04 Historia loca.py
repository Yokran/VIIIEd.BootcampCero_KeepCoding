#SOLUCIÓN:
# Sin función de sustitución

plantilla = "Un/a 0 1 debe 2 3"

nombre = input("Introduce un nombre: ")
verbo =  input("Introduce un verbo: ")
adjetivo =  input("Introduce un adjetivo: ")
adverbio =  input("Introduce un adverbio: ")

ix = 0
frase = ""

while ix < len(plantilla):
  car = plantilla[ix]
  
  if car == "0":
    frase = frase + nombre
  elif car == "1":
    frase = frase + adjetivo
  elif car == "2":
    frase = frase + verbo
  elif car == "3":
    frase = frase + adverbio
  else:
    frase = frase + car
    
  ix = ix + 1

  
print(frase)

# Usando format

plantilla = "Un/a {} {} debe {} {}"

nombre = input("Introduce un nombre: ")
verbo =  input("Introduce un verbo: ")
adjetivo =  input("Introduce un adjetivo: ")
adverbio =  input("Introduce un adverbio: ")

print(plantilla.format(nombre, adjetivo, verbo, adverbio))