def imprimeCosas(*listadecosas):
    for item in listadecosas:
        print(item)
        
def imprimecondiccionario(**diccionariodeparametros):
    if 'line' in diccionariodeparametros:
        print('Posicionar en line', diccionariodeparametros['line'])
    else:
        print('no hay line')
        
imprimeCosas('cosa 1', 'cosa 2', 'cosa 3', 'cosa 4')

imprimecondiccionario(contenido='la cosa', line=3, column=5)