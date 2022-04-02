#SOLUCIÓN:
strQ = input("Cantidad invertida: ")
strA = input("Años transcurridos: ")
strI = input("Interés anual: ")

Q = round(float(strQ), 2)
A = float(strA)
I = float(strI)/100

ganancia = Q * (1 + I * A)

print("Tras {} años de inversión al {:.2f}%, su cantidad debe ser {:.2f}€".format(A, I*100, ganancia))