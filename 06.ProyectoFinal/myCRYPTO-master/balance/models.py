from balance import app
from balance.controllers import *
import sqlite3

def consultaSQL(consulta):

    conexion = sqlite3.connect(BASE_DATOS)
    cursor = conexion.cursor()

    movimientos = cursor.execute(consulta).fetchall()

    if len(movimientos) == 0:
        movimientos = None

    conexion.commit()
    conexion.close()

    return movimientos

def saldoSQL():
    cryptoBalance = []
    for moneda in cryptos:
        cryptoBalanceCoin = consultaSQL('''
                                WITH BALANCE
                                AS
                                (
                                SELECT SUM(cantidad_from) AS saldo
                                FROM movements
                                WHERE moneda_to LIKE "%{}%"
                                UNION ALL
                                SELECT -SUM(cantidad_to) AS saldo
                                FROM movements
                                WHERE moneda_from LIKE "%{}%"
                                )
                                SELECT SUM(saldo)
                                FROM BALANCE
                                '''.format(moneda, moneda))
        if cryptoBalanceCoin[0] == (None,):
            cryptoBalanceCoin=0
            cryptoBalance.append(cryptoBalanceCoin)
        else:
            cryptoBalance.append(cryptoBalanceCoin[0][0])
    return cryptoBalance