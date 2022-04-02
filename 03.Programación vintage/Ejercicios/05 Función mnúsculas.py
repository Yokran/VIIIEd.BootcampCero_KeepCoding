mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

def minusculas(cadena):
  res = ""
  for caracter in cadena:
    if caracter in mayusculas:
      res += chr(ord(caracter)+32)
    else:
      res += caracter
  return res