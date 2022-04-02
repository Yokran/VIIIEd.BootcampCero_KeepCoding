digitos16 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
angulo = 360/16

cadena = "Hola"
for caracter in cadena:
    valorHexadecimal = hex(ord(caracter))
    digito1 = valorHexadecimal[2]
    angulo1 = digitos16.index(digito1) * angulo
    digito2 = valorHexadecimal[3]
    angulo2 = digitos16.index(digito2) * angulo
    print(digito1, '-', angulo1)
    print(digito2, '-', angulo2)