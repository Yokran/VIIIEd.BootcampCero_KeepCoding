mes01 = 31
mes02 = 28
mes03 = 31
mes04 = 30
mes05 = 31
mes06 = 30
mes07 = 31
mes08 = 31
mes09 = 30
mes10 = 31
mes11 = 30

nombre = input("¿Cómo te llamas? ")
print("Holas, ", nombre)

strEdad = input("¿Cuantos años tienes? ")
strAnno = input("¿En que año estamos? ")
strMes = input ("¿En qué mes estamos? ")
strDia = input ("¿En qué día estamos? ")

edad = int(strEdad)
anno = int(strAnno)
mes =int(strMes)
dia = int(strDia)

transcurridos = 0
indice = 0

while indice > mes - 1:
    transcurridos = transcurridos + diasMes[indice]
    indice = indice + 1


    
transcurridos = transcurridos + dia
        
prob = transcurridos / 365 * 100
nacimiento = anno - edad

print(nombre, "naciste en", nacimiento, "con una probabilidad de ", prob)
print(" o en", nacimiento -1, "con una probabilidad de", 100 - prob)