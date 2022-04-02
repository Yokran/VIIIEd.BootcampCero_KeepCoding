
   
       


p = input("Introduce tu contraseña: ")


def validaPwd (password):
    
    if len(p) < [8]:
        print("Contraseña muy debil")
    elif len(p) >= [8]:
        print("Contraseña fuerte")


'''
letters = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ " #Incluyo el espacio como letra pos si se admiten frases como pwd
numbers = "0123456789"

def veryWeakIndicator(pwd):
  res = False
  if len(pwd) < 8:
    res = True
    for i in range(0, len(pwd)):
      res = res and pwd[i] in numbers
  
  return res

def weakIndicator(pwd):
  res = False
  if len(pwd) < 8:
    res = True
    for i in range(0, len(pwd)):
      res = res and (pwd[i] in letters or pwd[i] in numbers) #He decidido que si es menor de 8 con letras y números es igual que menos de 8 letras

  return res

def strongIndicator(pwd):
  res = False
  leastOneNumber = 0
  if len(pwd) >= 8:
    res = True
    for i in range(0, len(pwd)):
      swNumber = pwd[i] in numbers
      leastOneNumber += 1 if swNumber else 0
      res = res and (pwd[i] in letters or swNumber)

  return res and leastOneNumber > 0

def veryStrongIndicator(pwd):
  res = False
  if len(pwd) >= 8:
    for i in range(0, len(pwd)):
      res = res or (pwd[i] not in letters and pwd[i] not in numbers)

  return res

def validaPwd(pwd):
  if veryStrongIndicator(pwd):
    return 3
  elif strongIndicator(pwd):
    return 2
  elif weakIndicator(pwd):
    return 1
  elif veryWeakIndicator(pwd):
    return 0
  else:
    return -1
 ''' 