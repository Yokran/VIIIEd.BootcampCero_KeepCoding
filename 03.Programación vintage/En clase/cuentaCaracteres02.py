miTexto = "tres palabras para ti."

frecuencias = dict()

for caracter in miTexto:
    if caracter in frecuencias:
#    if frecuencias.get(caracter) ! = None:
        frecuencias [caracter] +=1
    else:
        frecuencias[caracter] = 1
for letra in frecuencias.keys():
    print(letra, "-", frecuencias[letra])