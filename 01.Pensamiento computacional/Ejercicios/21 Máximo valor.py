strn1 = input("Introduce el primer número: ")
strn2 = input("Introduce el segundo número: ")
strn3 = input("Introduce el tercer número: ")

n1 = int(strn1)
n2 = int(strn2)
n3 = int(strn3)
ns = (n1,n2,n3)

while not ns!= int(ns)
    print("Fuera de rango")

if n1 > n2 and n3:
    print(n1)
elif n2 > n1 and n3:
    print(n2)
elif n3 > n1 and n2:
    print(n3)
    
#SOLUCIÓN:

n1 = ""
n2 = ""
n3 = ""
while n1 == "":
  try:
    n1 = int(input("Primer número: "))
  except:
    n1 = ""
    
while n2 == "" or n1 == n2:
  try:
    n2 = int(input("Segundo número: "))
  except:
    n2 = ""
    
while n3 == "" or n1 == n3 or n2 == n3:
  try:
    n3 = int(input("Tercer número: "))
  except:
    n3 = ""
    
max = None
if n1 > n2:
  if n1 > n3:
    max = n1
  else:
    max = n3
else:
  if n2 > n3:
    max = n2
  else:
    max = n3
    
print("El mayor es: {}".format(max))