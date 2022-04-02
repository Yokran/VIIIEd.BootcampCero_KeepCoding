def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

cadenaBase = input("Base del triángulo: ")
if esDecimal(cadenaBase):
    base=float(cadenaBase)
else:
    print(cadenaBase, "debe ser un número")
    quit() 
cadenaAltura = input("Altura del triángulo: ")

base = float(cadenaBase)
altura = float(cadenaAltura)

area = base * altura / 2

print("Superficie del triángulo:", round(area, 2))