import screen
import presentacion
from config import preciosE, entradasQ

numEntradas = {'bebe': 0, 'niño': 0, 'adulto': 0, 'jubilado': 0}

def tipoEntrada(e):
    if e > 0 and e <=2:
        tipo = 'bebe'
    elif e <= 12:
        tipo = 'niño'
    elif e < 65:
        tipo = 'adulto'
    else:
        tipo = 'jubilado'
    
    return tipo 

def main():    
    presentacion.printScreen()

    edad = presentacion.pedirEdad()
    precioTotal = 0

    while edad != 0:
        tipoE = tipoEntrada(edad)
        precioE = preciosE[tipoE]
        
        numEntradas[tipoE] += 1
        
        screen.Print(numEntradas[tipoE],
                     line=entradasQ[tipoE]['cantidad'][0],
                     column=entradasQ[tipoE]['cantidad'][1])
                    
        screen.Print("{:7.2f}€".format(numEntradas[tipoE]*precioE),
                     line=entradasQ[tipoE]['precioA'][0],
                     column=entradasQ[tipoE]['precioA'][1])
        
        
        
        precioTotal += precioE
        screen.Print("{:7.2f}€".format(precioTotal),
                     line=9, column=19) 
        edad = presentacion.pedirEdad()
     
    fEntradas = open('transacciones.txt', 'a+')
    transaccion = "{},{},{},{}\n".format(numEntradas['bebe'], numEntradas['niño'], numEntradas['adulto'], numEntradas['jubilado'])
    
    fEntradas.write(transaccion)
    
    fEntradas.close()
    screen.locate(11, 1) 


main()





