def myUpper(cadena):
    resultado = ""
    
    for caracter in cadena:
        nuevoCaracter = ord(caracter)-32
        resultado += chr(nuevoCaracter)