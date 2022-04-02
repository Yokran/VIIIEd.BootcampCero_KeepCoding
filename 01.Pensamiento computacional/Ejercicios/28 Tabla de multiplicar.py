strvalor = int(input("Introduzca valor: "))



while strvalor < 0:
    print("¡Ha escrito un número negativo o no entero! Inténtelo de nuevo")
    strvalor = int(input("Introduzca valor: "))

valor = int(strvalor)

v1 = valor * 1
v2 = valor * 2
v3 = valor * 3
v4 = valor * 4
v5 = valor * 5
v6 = valor * 6
v7 = valor * 7
v8 = valor * 8
v9 = valor * 9
v10 = valor * 10

print("{} x 1 = {}".format(valor,v1))
print("{} x 2 = {}".format(valor,v2))
print("{} x 3 = {}".format(valor,v3))
print("{} x 4 = {}".format(valor,v4))
print("{} x 5 = {}".format(valor,v5))
print("{} x 6 = {}".format(valor,v6))
print("{} x 7 = {}".format(valor,v7))
print("{} x 8 = {}".format(valor,v8))
print("{} x 9 = {}".format(valor,v9))
print("{} x 10 = {}".format(valor,v10))

#SOLUCIÓN:
def intValue(n):
  try:
    resultado = int(n)
  except:
    resultado = None
  return resultado

numero = None
while numero == None:
  strNumero = input("Introduzca valor: ")
  numero = intValue(strNumero)
  
for i in range(1, 11):
  print("{} x {} = {}".format(numero, i, numero * i))