import screen

def validaEdad(cadena):
    try:
        n = int(cadena)
        if n>=0:
            
            return True
        return False
    except:
        return False

def pedirEdad():
    edad = screen.Input("¿Qué edad tienes?", 1, 1)
    while validaEdad(edad) == False:
        screen.Format(0, 33, 41)        
        screen.Print("Edad invalida", 25, 1, True)
        screen.Reset()
        edad = screen.Input("¿Qué edad tienes?", 1, 1)
    
    screen.clearline(25)
  
    
    return int(edad)

def printScreen():
    screen.clear()
    screen.Print("bebe....:   -", 4, 5)  
    screen.Print("niño....:   -", 5, 5)   
    screen.Print("adulto..:   -", 6, 5)   
    screen.Print("jubilado:   -", 7, 5)
        
    screen.Format(1)
    screen.Print("Total.....:", 9, 8)