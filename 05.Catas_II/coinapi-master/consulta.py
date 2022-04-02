import requests

url = 'https://rest.coinapi.io/v1/exchangerate/BTC/EUR'
apikey = "BE728918-EFE1-4116-95B6-4E8F7F54B5DC"

cabecera = {"X-CoinAPI-Key": apikey}
respuesta = requests.get(url, headers=cabecera)

print(respuesta.status_code)
midiccionario = respuesta.json()
print(midiccionario["rate"])

# print(respuesta.json()["rate"])
