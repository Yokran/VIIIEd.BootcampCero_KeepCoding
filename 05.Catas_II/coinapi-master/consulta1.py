import requests

url = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'
apikey = "BE728918-EFE1-4116-95B6-4E8F7F54B5DC"

cabecera = {"X-CoinAPI-Key": apikey}


mas = True

seguir = "s"

while seguir == "s":
    de = input("Moneda de origen ")
    a = input("Moneda de destino ")
    respuesta = requests.get(url.format(de, a), headers=cabecera)

    if respuesta.status_code == 200:
        print(respuesta.json()["rate"])
    else:
        print(respuesta.status_code)
        print(respuesta.json())

    seguir = input("Quieres más (S/N) ").lower()
