import statistics as stats

strv1 = input("Introduzca un valor...................")
strv2 = input("Introduzca otro o finalice con 0......")
strv3 = input("Introduzca otro o finalice con 0......")
strv4 = input("Introduzca otro o finalice con 0......")
strv5 = input("Introduzca otro o finalice con 0......")
strv6 = input("Introduzca otro o finalice con 0......")
strv7 = input("Introduzca otro o finalice con 0......")
strv8 = input("Introduzca otro o finalice con 0......")

v1 = float(strv1)
v2 = float(strv2)
v3 = float(strv3)
v4 = float(strv4)
v5 = float(strv5)
v6 = float(strv6)
v7 = float(strv7)
v8 = float(strv8)

media = [v1, v2, v3, v4, v5, v6, v7, v8]

print(stats.mean(media))

#SOLUCIÓN:
def floatValue(n):
  try:
    resultado = float(n)
  except:
    resultado = None
  return resultado

total = 0
contador = 0
numero = None

while numero != 0:
    strNumero = input("Introduce valor: ")
    numero = floatValue(strNumero)
    while numero == None:
      print ("{} debe ser un número".format(strNumero))
      strNumero = input("Introduce valor: ")
      numero = floatValue(strNumero)
    total = total + numero
    contador = contador + 1

if contador == 1:
  print("No se han introducido valores")
else:
  media = total / (contador - 1)
  print("Media = {}/{} = {}".format(total, contador-1, media))