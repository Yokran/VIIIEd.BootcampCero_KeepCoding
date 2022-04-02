original = input("Introduce palabra original: ")
nueva = input("Introduce palabra nueva: ")

nombreF = "fichero.txt"

f = open(nombreF, "r")

texto_original = f.read()
f.close()

texto_sustituido = texto_original.replace(original, nueva)

f = open(nombreF, "w")

f.write(texto_sustituido)
f.close()