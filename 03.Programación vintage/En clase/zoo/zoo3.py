import screen

def calcularPrecioEntrada(e):
    if e > 0 and e <=2:
        precio = 0
    elif e <= 2:
        precio = 14
    elif e < 65:
        precio = 23
    else:
        precio = 18
    
    return precio

def validaEdad(cadena):
    try:
        n = int(cadena)
        if n>=0:
            
            return True
        return False
    except:
        return False

def pedirEdad():
    screen.locate(1,1)
    edad = input("¿Que edad tienes? ")
    while validaEdad(edad) == False:
        print("Edad invalida")
        screen.locate(1,1)
        edad = input("¿Que edad tienes? ")
    
    return int(edad)

screen.clear()
edad = pedirEdad()
precioTotal = 0
linea = 4

while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    screen.locate(linea, 1)
    print("Precio Entrada: {}".format(precioE))
    linea += 1
    precioTotal += precioE
    
    edad = pedirEdad()
    
print("Total: {}".format(precioTotal))


