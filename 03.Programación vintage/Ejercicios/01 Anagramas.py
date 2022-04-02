def esAnagrama(p1, p2):
    listaComparacionletras = []
    

    if len(p1) != len(p2):
        return False
        print("No es un Anagrama")
    else:
        return True
    
    for caracter1
        
   '''     
        
 def isAnagram(c1, c2):
  if len(c1) != len(c2):
    return False 

  lc2 = list(c2)
  for i in range(0, len(c1)):
    print(lc2)
    for j in range(0, len(c2)):
      if c1[i] == lc2[j]:
        lc2[j] = '*'
        break
  
  print(lc2)
        
  comp = '*'*len(c2)
  c2 = "".join(lc2)
  print(comp, 'vs', c2)
  return comp == c2

def isAnagramI(c1, c2):
  if len(c1) != len(c2):
    return False 
  
  posi = []

  for i in range(0, len(c1)):  
    print(posi)
    for j in range(0, len(c2)):
      if c1[i] == c2[j] and j not in posi:
        posi.append(j)
  
  print(posi)
  return len(posi) == len(c2)
  
       '''
