def isAnagramEle(p1, p2):
    listaComparacionLetras = []
    
    if len(p1) != len(p2):
        return False
    
    for caracter1 in p1:
        noAñadasFalse = False
        for caracter2 in p2:
            if caracter1 == caracter2:
                noAñadasFalse = True
                listaComparacionLetras.append(True)
                
            if not noAñadasFalse:
                listaComparacionLetras.append(False)
        
        if False in listaComparacionLetras:
            return False
        else:
            return True
def isAnagram(p1, p2):
    return isAnagramEle(p1, p2) and isAnagramEle(p2, p1)


