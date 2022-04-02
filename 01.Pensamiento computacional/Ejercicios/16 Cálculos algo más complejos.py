#SOLUCIÓN
def inputInt(msg):
  val = ""
  while val == "":
    cad = input(msg)
    try:
      val = int(cad)
    except:
      val = ""

  return val

def inputFloat(msg):
  val = ""
  while val == "":
    cad = input(msg)
    try:
      val = float(cad)
    except:
      val = ""

  return val


strMas = "S"
alcoholAbsoluto = 0
while strMas == "S":
  bebidas = inputInt("Número de bebidas: ")
  volumen = inputInt("Volumen por bebida en cc: ")
  grado = inputFloat("Grado alcohólico: ")
  
  alcoholAbsoluto += bebidas * volumen * grado * 0.8 / 100
  
  strMas = input("Otra bebida(S/N) ")
  
UBE = alcoholAbsoluto / 10
horas = inputFloat("Horas transcurridas: ")

BAC = UBE*0.3 - horas * 0.15

print("Alcohol en sangre: {} g/l".format(BAC))
print("El máximo permitido es 0.5 g/l")
if BAC > 0.5:
  print("Usted no puede conducir")
else:
  print("Usted puede conducir")