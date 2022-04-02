Hungria = 27
Croacia = 25
Dinamarca = 25
Suecia = 25
Finlandia = 24
Rumania = 24
Grecia = 23
Irlanda = 23
Polonia = 23
Portugal = 23
Eslovenia = 22
Italia = 22
Espana = 21
Belgica = 21
Letonia = 21
Lituania = 21
PaisesBajos = 21
RepublicaCheca = 21
Austria = 20
Bulgaria = 20
Eslovaquia = 20
Estonia = 20
Francia = 20
ReinoUnido = 20
Alemania = 19
Chipre = 19
Malta = 18
Luxemburgo = 15

strbase = input("Introduzca el importe: ")
pais = input("Introduzca el pais de residencia: ")

base = float(strbase)

if pais == "España":
    iva = 21
    ivatotal = round(base * 21 / 100,2)
    preciototal = base + ivatotal
    print("Base {} euros, iva aplicado {} %, iva correspondiente {} euros, precio total {} euros.".format(base,iva,ivatotal,preciototal))
    
#SOLUCIÓN:
ivas = {
    "hungria": 27,
    "croacia": 25,
    "dinamarca": 25,
    "suecia": 25,
    "finlandia": 24,
    "rumania": 24,
    "grecia": 23,
    "irlanda": 23,
    "polonia": 23, 
    "portugal": 23,
    "eslovenia": 22,
    "italia": 22,
    "españa": 21,
    "belgica": 21,
    "letonia": 21,
    "lituania": 21,
    "paises bajos": 21,
    "republica checa": 21,
    "austria": 20,
    "bulgaria": 20,
    "eslovaquia": 20,
    "estonia": 20,
    "francia": 20,
    "reino unido": 20,
    "alemania": 19,
    "chipre": 19,
    "malta": 18,
    "luxemburgo": 19
}

strPais = input("País de origen: ")
strPais.lower()
strPrecio = input("Precio: ")

precio = round(float(strPrecio), 2)

if ivas.get(strPais):
  iva = precio *  ivas[strPais]/100
else:
  iva = 0
  
total = precio + iva

print("Base: {:0.2f}€\nIVA: {}% - {:0.2f}€\nTotal: {:0.2f}€".format(precio, ivas[strPais], iva, total) if ivas.get(strPais) else "País no conocido")
    