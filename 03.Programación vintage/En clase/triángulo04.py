def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

cadenaBase = input("Base del triángulo: ")
while not esDecimal(cadenaBase):
    print(cadenaBase, "debe ser un número")
    cadenaBase = input("Base del triángulo: ")

cadenaAltura = input("Altura del triángulo: ")
while not esDecimal(cadenaAltura):
    print(cadenaAltura, "debe ser un número")
    cadenaAltura = input("Altura del triángulo: ")
base = float(cadenaBase)
altura = float(cadenaAltura)
area = base * altura / 2
print("Superficie del triángulo:", round(area, 2))