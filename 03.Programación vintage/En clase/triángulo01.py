cadenaBase = input("Base del triángulo: ")
cadenaAltura = input("Altura del triángulo: ")

base = float(cadenaBase)
altura = float(cadenaAltura)

area = base * altura / 2

print("Superficie del triángulo:", round(area, 2))