def myUpper(cadena):
    resultado = ""
    
    for caracter in cadena:
        codigoCaracter = ord(caracter)
        if codigoCaracter >= 97 and codigoCaracter <=122:
            codigoMays = codigoCaracter - 32
            caracterMays = chr(codigoMays)
            resultado = resultado + caracterMays
        else:
            resultado = resultado + caracter
            
    return resultado

palabras = input("dime algo bajito:")
print("yo te grito:", myUpper(palabras))