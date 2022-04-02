tupla = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

indice = 0
contadorkill = indice + 1

while indice < len(tupla):
    if contadorkill == 3 or contadorkill == 6 or contadorkill == 9:
        mataletra()
    indice += 1


while indice < len(tupla):
    if(indice + 1) % 3 == 0:
        print(tupla[indice])
    indice += 1