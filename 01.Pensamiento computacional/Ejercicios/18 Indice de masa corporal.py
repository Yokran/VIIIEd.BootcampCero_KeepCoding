strpeso = input("Introduce tu perso exacto....... ")
straltura = input("Introduce tu altura exacta.... ")

peso = float(strpeso)
altura = float (straltura)

strimc = peso / (altura**2)

imc = float(strimc)

print("Tu Indice de masa corporal es", imc)

if imc < 18 > 15:
    print("Tu peso se considera normal")

elif imc > 18:
    print("Estas gordo, haz dieta y ejercicio")

else imc < 18:
    print("Eres flacucho, necesitas un puchero")
    
#SOLUCIÓN:

peso = ""
while peso == "":
  cad = input("Peso: ")
  try:
    peso = float(cad)
  except:
    peso = ""

altura = ""
while altura == "":
  cad = input("Altura: ")
  try:
    altura = float(cad)
  except:
    altura = ""

imc = peso/altura**2

print("Tu índice de masa corporal es {:.2f}".format(imc))
if imc < 18.5:
  print("Estas muy delgado, quizás deberías visitar a tu médico.")
elif imc > 15:
  print("Tienes sobrepeso, quizás deberías visitar a tu médico.")
else:
  print("Estas en tu peso ideal")