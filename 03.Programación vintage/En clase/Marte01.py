digitos16 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
angulo = 360/16

cadena = "Hola"
for caracter in cadena:
    valorHexadecimal = hex(ord(caracter))
    digito1 = valorHexadecimal[2]
    digito2 = valorHexadecimal[3]
    print(digito1)
    print(digito2)