from config import preciosE

fEntradas = open("transacciones.txt", 'r')

numEntradasBebe = 0
numEntradasNino = 0
numEntradasAdulto = 0
numEntradasJubilado = 0

linea = fEntradas.readline()

totalEntradas = 0
totalPrecios = 0


while linea != '':
    entradas = linea.split(',')
    numEntradasBebe += int(entradas[0])    
    numEntradasNino += int(entradas[1])
    numEntradasAdulto += int(entradas[2])
    numEntradasJubilado += int(entradas[3])
    
    totalEntradas = totalEntradas + int(entradas[0])
    totalEntradas = totalEntradas + int(entradas[1])
    totalEntradas = totalEntradas + int(entradas[2])
    totalEntradas = totalEntradas + int(entradas[3])       
            
    linea = fEntradas.readline()
    
print("Entradas de Bebe......: {:3d} - {:7.2f}".format(numEntradasBebe, numEntradasBebe * preciosE['bebe']))
print("Entradas de Niño:.....: {:3d} - {:7.2f}".format(numEntradasNino, numEntradasNino * preciosE['niño']))
print("Entradas de Adulto....: {:3d} - {:7.2f}".format(numEntradasAdulto, numEntradasAdulto * preciosE['Adulto']))
print("Entradas de Jubilado..: {:3d} - {:7.2f}".format(numEntradasJubilado, numEntradasJubilado * preciosE['Jubilado']))

print("\Total: {:3d} - {:7.2f}€".format(totalEntradas, numEntradasBebe * preciosE['bebe']+numEntradasNino * preciosE['niño']+\
                                        numEntradasAdulto * preciosE['adulto']+numEntradasBebe * preciosE['bebe']))