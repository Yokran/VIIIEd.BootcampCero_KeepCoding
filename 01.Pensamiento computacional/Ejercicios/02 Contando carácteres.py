str = input("Escribe algo: ")

print("La cadena '", str, "' tiene", len(str), "caracteres")

#SOLUCIÓN:

str = input("Escribe algo: ")

print("La cadena '", str, "' tiene", len(str), "caracteres")
print("La cadena '{}' tiene {} caracteres".format(str, len(str)))

original = input("Escribe algo: ")

str = original
contador = 0

while str != "":
  str = str[1:]
  contador += 1

print("La cadena '{}' tiene {} caracteres".format(original, contador))