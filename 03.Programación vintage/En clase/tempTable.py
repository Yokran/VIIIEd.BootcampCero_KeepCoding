def fahrenheitToCentigrados(g):
    return (g - 32) * 5/9

def centigradosToFarenheit(g):
    return g * 5/9 + 32

def centigrados(ini, fin):
    for grados in range(ini, fin+10, 10):
        print("{}ºF -> {}ºC".format(grados, fahrenheitToCentigrados(grados)))

def farenheit(ini, fin):
    for grados in range(ini, fin, 10):
        print("{}ºC -> {}ºF".format(grados, centigradosToFarenheit(grados)))

tipo = input("Salida (F/C): ").lower()

if tipo == 'c':
    centigrados(0, 230)
elif tipo == 'f':
    farenheit(0, 100)
else:
    print("Tipo incorrecto")