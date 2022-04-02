# Entrada de datos
strNumero01 = input("Introduce el primer número: ")
strNumero02 = input("Introduce el segundo número: ")

if strNumero01.isdigit():
    numero01 = int(strNumero01)
elif strNumero01 [0] == "-" and strNumero01[1:].isdigit():
    numero01 = int(strNumero01)
else:
    print(strNumero01, "debe ser un entero")
    quit()

if strNumero02.isdigit():
    numero02 = int(strNumero02)
elif strNumero02 [0] == "-" and strNumero01[1:].isdigit():
    numero02 = int(strNumero02)
else:
    print(strNumero02, "debe ser un entero")
    quit()
    
# Procesamiento de datos

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