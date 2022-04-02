def validacion(mensaje):
    strNumero = input(mensaje)

    isvalid = False
    while not isvalidN01:
        if strNumero.isdigit():
            numero = int(strNumero)
            isvalid = True
        elif strNumero!= '' and strNumero[0] == '-' and strNumero[1:].isdigit():
            numero = int(strNumero)
            isvalidN = True
        else:
            print(strNumero, "debe ser un entero")
            strNumero = input(mensaje)

    return strNumero

strNumero01 = validacion("Introduce el primer número: ")

strNumero02 = validacion("Introduce el segundo número: ")
    
# Procesamiento de datos
numero01 = int(strNumero01)
numero02 = int(strNumero02)

 
numero01 = numero01/10
numero02 = numero02/10

suma = round(numero01 + numero02,2)
resta = round(numero01 - numero02,2)
producto = numero01 * numero02
producto = round(producto, 2)
division = numero01 / numero02
division = round (division, 2)

# Salida de resultados
print(numero01, "+", numero02, "=", suma)
print(numero01, "-", numero02, "=", resta)
print(numero01, "*", numero02, "=", producto)
print(numero01, "/", numero02, "=", division)