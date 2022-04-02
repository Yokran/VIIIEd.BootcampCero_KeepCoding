strTemperatura = input("Dame la temperatura: ")
Celsiusfaren = input("El valor dado es en Celsius 'C' o en Farenheit 'F': ")

if Celsisusfaren == "F":
       ConFaren = input("¿Quieres ver el resultado en grados Celsius? S o N")
elif ConFaren == "S":
     rcelsius = (float(strTemperatura)-32)*(5/9)
     print(rcelsius)
    
#SOLUCIÓN:

strTipo = input("Temperatura de entrada en Fahrenheit o Celsius (F/C)")
strTemp = input("Valor de la temperatura: ")

temp = float(strTemp)

if strTipo == 'c' or strTipo == 'C':
  strIN = 'C'
  strOUT = 'F'
  output = (temp * 9/5) + 32
else:
  strIN = 'F'
  strOUT = 'C'
  output = (temp - 32) * 5/9
  
print("\n{}º{} son {}º{}".format(temp, strIN, output, strOUT))



