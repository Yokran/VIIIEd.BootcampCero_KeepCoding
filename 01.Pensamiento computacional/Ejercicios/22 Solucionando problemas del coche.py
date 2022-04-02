import time

arranca = input("¿Arranca? S o N .......")

if arranca == "S":
    suena = input("¿Suena un clic-clic? S o N .......")
    if suena == "S":
        print("Reemplaza la bateria")
    if suena == "N":
        enciende = input("¿Se enciende el coche pero no arranca? S o N .......")    
    else:
        print("No has introducido una respuesta correcta y el coche va a explotar")

        
        if enciende == "S":
            print("Revisa las bujias")
        if enciende == "N":
            cala = input("¿Arranca el coche y luego se cala? S o N .......")
        else:
            print("No has introducido una respuesta correcta y el coche va a explotar")
    
            
            if cala == "S":
              inyeccion = input("¿Tiene el coche inyección de combustible? S o N .......")
              
            if cala == "N":
                  print("Lleve el coche al taller")
            else:
                print("No has introducido una respuesta correcta y el coche va a explotar")
              
                if inyeccion == "S":
                   print("Lleve el coche al taller")
                if inyeccion == "N":
                   print("Abre y cierra el starter")
                else:
                    print("No has introducido una respuesta correcta y el coche va a explotar")

  
elif arranca == "N":
    bornes = input("¿Están los bornes de la batería corroídos? S o N .......")
    
    if bornes == "S":
        print("Limpia los bornes y arranca de nuevo")
    if bornes == "N":
        print("Reemplaza los cables y arranca de nuevo")
    else:
        print("No has introducido una respuesta correcta y el coche va a explotar")

else:
    print("No has introducido una respuesta correcta y el coche va a explotar")
    
#SOLUCIÓN:
    
strResp = input("¿Arranca? ")
solucion = "Todo parece OK"
if strResp.lower() == 's':
  strResp = input("¿Suena un clic-clic? ")
  if strResp.lower() == 's':
    solucion = "Reemplaza la batería"
  else: 
    strResp = input("¿Se enciende el coche pero no arranca? ")
    if strResp.lower() == 's':
      solucion = "Revisa las bujías"
    else:
      strResp = input("¿Arranca el coche y luego se cala? ")
      if strResp.lower() == 's':
        strResp = input("¿Es un coche de inyección ")
        if strResp.lower() == 's':
          solucion = "Lleve el coche al taller"
        else:
          solucion = "Abra y cierre el starter"
else:
  strResp = input("¿Están los bornes de la batería corroidos? ")
  if strResp.lower() == 's':
    solucion = "Limpia los bornes y arranca de nuevo"
  else:
    solucion = "Reemplaza los cables y arranca de nuevo"

print("Entonces...\n", solucion)

