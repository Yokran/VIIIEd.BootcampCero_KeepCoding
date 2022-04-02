from balance import app
import json
from requests import Session

BASE_DATOS = app.config.get("RUTA_BASE_DATOS")
API_KEY=app.config['API_KEY']

cryptos = ("BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "USDT", "EOS", "BSV", "XLM", "ADA", "TRX")

def api(fromApi, toApi):

    url= "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1&symbol={}&convert={}&CMC_PRO_API_KEY=<API_KEY>".format(fromApi, toApi)

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    }

    session = Session()
    session.headers.update(headers)

    respuesta = session.get(url)
    data = json.loads(respuesta.text)
    try:
        return ('', data['data']['quote'][toApi]['price'])
    except:
        errorCodeAPI = data['status']['error_code']
        return ('error', errorCodeAPI)

def errorApi(codigo):
    if codigo == 1001:
        respuestaError = "La API KEY no es válida"
    elif codigo == 1002:
        respuestaError= "No existe API KEY"
    elif codigo == 1003:
        respuestaError= "La API KEY no está activada"
    elif codigo == 1004:
        respuestaError= "La API KEY ha caducado"
    elif codigo == 1005:
        respuestaError= "Se requiere API KEY"
    elif codigo == 1006:
        respuestaError= "API KEY incompatible con esta operación"
    elif codigo == 1007:
        respuestaError= "API KEY deshabilitada"
    elif codigo == 1008:
        respuestaError= "Excedido límite de velocidad de solicitud HTTP de la API KEY"
    elif codigo == 1009:
        respuestaError= "Excedido límite de tarifa diaria de API KEY"
    elif codigo == 1010:
        respuestaError= "Excedido límite de tarifa mensual de API KEY"
    elif codigo == 1011:
        respuestaError= "Alcanzado límite de velocidad de la IP"

    return respuestaError