def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

cadenaBase = input("Base del triángulo: ")
if esDecimal(cadenaBase):
    cadenaAltura = input("Altura del triángulo: ")
    if esDecimal(cadenaAltura):
        base = float(cadenaBase)
        altura = float(cadenaAltura)
        area = base * altura / 2
        print("Superficie del triángulo:", round(area, 2))
    else:
        print(cadenaAltura, "debe ser un número")
        quit()  
else:
    print(cadenaBase, "debe ser un número")
    quit() 


