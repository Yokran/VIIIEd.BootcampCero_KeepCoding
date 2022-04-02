from balance import app
from balance.controllers import *
from balance.models import *
from flask import render_template, request, redirect, url_for
from balance.forms import CompraFormulario
import datetime
import sqlite3

@app.route("/")
def inicio():
        try:
            registros = consultaSQL("SELECT date, time, moneda_from, cantidad_from, moneda_to, cantidad_to FROM movements;")
            return render_template("inicio.html", menu ='inicio', registros = registros)

        except sqlite3.Error:
            registros = None
            error_base_datos = "ERROR EN LA BASE DE DATOS"
            return render_template("inicio.html", menu ='inicio', error_base_datos = error_base_datos, registros = registros)

@app.route("/purchase", methods=['GET', 'POST'])
def purchase():

    form = CompraFormulario(request.form)
    fromMoneda=request.values.get("from_moneda")
    toMoneda=request.values.get("to_moneda")
    datoCantidad=request.values.get("to_cantidad")
    cantidad = 0
    precioUnitario = 0

    if request.method == 'GET':

        return render_template("purchase.html", menu = 'purchase', form = form, data = [cantidad,precioUnitario])

    if request.values.get("submitCalcular"):
        if not form.validate():
            cantidad = 0
            precioUnitario = 0
            validaError = "LA CANTIDAD DEBE SER NUMÉRICA Y SUPERIOR A 0"
            return render_template("purchase.html", menu = 'purchase',form = form , validaError = validaError, data = [cantidad,precioUnitario])

        if fromMoneda == toMoneda:
            cantidad = 0
            precioUnitario = 0
            monedaError = "SI NO SELECCIONAS DOS MONEDAS DISTINTAS ¿QUE COÑO VAS A INVERTIR?"
            return render_template("purchase.html", menu = 'purchase',form = form , monedaError = monedaError, data = [cantidad,precioUnitario])

        if fromMoneda == 'EUR' and toMoneda != 'BTC':
            cantidad = 0
            precioUnitario = 0
            monedaIncompatible = "NO PUEDES COMPRAR {} CON EUROS".format(toMoneda)
            return render_template("purchase.html", menu = 'purchase',form = form , monedaIncompatible = monedaIncompatible, data = [cantidad,precioUnitario])

        if toMoneda == 'EUR'and fromMoneda != "BTC":
            cantidad = 0
            precioUnitario = 0
            monedaIncompatible = "NO PUEDES COMPRAR EUROS CON {}".format(fromMoneda)
            return render_template("purchase.html", menu = 'purchase', form = form , monedaIncompatible = monedaIncompatible, data = [cantidad,precioUnitario])

        consultaApi = api(fromMoneda, toMoneda)
        if consultaApi[0] =='error':
            cantidad = 0
            precioUnitario = 0
            mensajeError = errorApi(consultaApi[1])
            errorAPI = "ERROR EN LA API - {}".format(mensajeError)
            return render_template("purchase.html", menu = 'purchase', form = form , errorAPI = errorAPI, data = [cantidad,precioUnitario])
        else:
            toCantidad = consultaApi[1]

        cantidad = float(toCantidad)*float(datoCantidad)
        precioUnitario = float(datoCantidad) / float(cantidad)

        return render_template("purchase.html", menu = 'purchase', form = form, data = [cantidad, precioUnitario, toMoneda, fromMoneda])

    if request.values.get("submitAceptar"):

        if not form.validate():
            cantidad = 0
            precioUnitario = 0
            validaError = "LA CANTIDAD DEBE SER NUMÉRICA Y SUPERIOR A 0"
            return render_template("purchase.html", menu = 'purchase', form = form , validaError = validaError, data = [cantidad,precioUnitario])

        if fromMoneda == toMoneda:
            cantidad = 0
            precioUnitario = 0
            monedaError = "SI NO SELECCIONAS DOS MONEDAS DISTINTAS ¿QUE COÑO VAS HA INVERTIR?"
            return render_template("purchase.html", menu = 'purchase', form = form , monedaError = monedaError, data = [cantidad,precioUnitario])

        if fromMoneda == 'EUR' and toMoneda != 'BTC':
            cantidad = 0
            precioUnitario = 0
            monedaIncompatible = "NO PUEDES COMPRAR {} CON EUROS".format(toMoneda)
            return render_template("purchase.html", menu = 'purchase', form = form , monedaIncompatible = monedaIncompatible, data = [cantidad,precioUnitario])

        if toMoneda == 'EUR'and fromMoneda != "BTC":
            cantidad = 0
            precioUnitario = 0
            monedaIncompatible = "NO PUEDES COMPRAR EUROS CON {}".format(fromMoneda)
            return render_template("purchase.html", menu = 'purchase', form = form , monedaIncompatible = monedaIncompatible, data = [cantidad,precioUnitario])

        if fromMoneda == 'EUR':
            saldo = 9999999999
        else:
            try:
                saldoInversion = consultaSQL('''
                            WITH BALANCE
                            AS
                            (
                            SELECT SUM(cantidad_to) AS saldo
                            FROM movements
                            WHERE moneda_to LIKE "%{}%"
                            UNION ALL
                            SELECT -SUM(cantidad_from) AS saldo
                            FROM movements
                            WHERE moneda_from LIKE "%{}%"
                            )
                            SELECT SUM(saldo)
                            FROM BALANCE;
                            '''.format(fromMoneda, fromMoneda))
            except sqlite3.Error:
                cantidad = 0
                precioUnitario = 0
                error_base_datos = "ERROR EN LA BASE DE DATOS"
                return render_template("purchase.html", menu = 'purchase', form = form , error_base_datos = error_base_datos, data = [cantidad,precioUnitario])

            if saldoInversion[0] == (None,):
                saldo = 0
            else:
                saldo = saldoInversion[0][0]

        if fromMoneda == 'EUR' or saldo != 0:

            dt = datetime.datetime.now()
            fecha=dt.strftime("%d/%m/%Y")
            hora=dt.strftime("%H:%M:%S")
            consultaApi = api(fromMoneda, toMoneda)
            if consultaApi[0] =='error':
                cantidad = 0
                precioUnitario = 0
                mensajeError = errorApi(consultaApi[1])
                errorAPI = "ERROR EN LA API - {}".format(mensajeError)
                return render_template("purchase.html", menu = 'purchase', form = form , errorAPI = errorAPI, data = [cantidad,precioUnitario])
            else:
                toCantidad = consultaApi[1]
                cantidad = float(toCantidad)*float(datoCantidad)

            if saldo >= cantidad or fromMoneda == 'EUR':

                conexion = sqlite3.connect(BASE_DATOS)
                cursor = conexion.cursor()
                movimiento = "INSERT INTO movements(date, time, moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES(?, ?, ?, ?, ?, ?);"

                try:
                    cursor.execute(movimiento, (fecha, hora, fromMoneda, float(cantidad), toMoneda, float(datoCantidad)))
                except sqlite3.Error:
                    cantidad = 0
                    precioUnitario = 0
                    error_base_datos = "ERROR EN LA BASE DE DATOS"
                    return render_template("purchase.html", menu = 'purchase', form = form , error_base_datos = error_base_datos, data = [cantidad,precioUnitario])

                conexion.commit()
                try:
                    registros = consultaSQL("SELECT date, time, moneda_from, cantidad_from, moneda_to, cantidad_to FROM movements;")
                    conexion.close()
                    return render_template("inicio.html", menu = 'inicio', form = form, registros = registros)
                except sqlite3.Error:
                    cantidad = 0
                    precioUnitario = 0
                    error_base_datos = "ERROR EN LA BASE DE DATOS"
                    return render_template("purchase.html", menu = 'purchase', form = form , error_base_datos = error_base_datos, data = [cantidad,precioUnitario])
            else:
                precioUnitario = toCantidad
                sinSaldo = "NO TIENES SALDO SUFICIENTE EN {} PARA REALIZAR ESTA OPERACIÓN".format(fromMoneda)
                return render_template("purchase.html", menu = 'purchase', form = form , sinSaldo=sinSaldo, data = [cantidad,precioUnitario])
        else:
            cantidad = 0
            precioUnitario = 0
            alerta = "NO EXISTE SALDO DE COMPRA EN LA CRYPTOMONEDA {}".format(fromMoneda)
            return render_template("purchase.html", menu = 'purchase', form = form, data = [cantidad, precioUnitario, toMoneda, fromMoneda], alerta = alerta)

@app.route("/status")
def inversion():

    try:
        noHayMovimiento = consultaSQL("SELECT date, time, moneda_from, cantidad_from, moneda_to, cantidad_to FROM movements;")
    except sqlite3.Error:
        totalInversion = 0
        valorActual = 0
        dif = 0
        error_base_datos = "ERROR EN LA BASE DE DATOS"
        return render_template("status.html", menu = 'status', error_base_datos = error_base_datos, noHayMovimiento = True)

    if noHayMovimiento == None:
        return render_template("status.html", menu = 'status', noHayMovimiento = True)

    try:
        fromInversion = consultaSQL('SELECT SUM(cantidad_from) FROM movements WHERE moneda_to LIKE "%EUR%";')
        toInversion = consultaSQL('SELECT SUM(cantidad_to) FROM movements WHERE moneda_from LIKE "%EUR%";')
    except sqlite3.Error:
        totalInversion = 0
        valorActual = 0
        dif = 0
        error_base_datos = "ERROR EN LA BASE DE DATOS"
        return render_template("status.html", menu = 'status', error_base_datos = error_base_datos, noHayMovimiento = True)

    totalInversionFrom = 0
    totalInversionTo = 0
    for i in range(len(toInversion)):
        if fromInversion[i] == (None,):
            totalInversionFrom += 0
        else:
            inversionFromInt = fromInversion[i][0]
            totalInversionFrom += inversionFromInt

    for i in range(len(fromInversion)):
        if toInversion[i] == (None,):
            totalInversionTo += 0
        else:
            inversionToInt = toInversion[i][0]
            totalInversionTo += inversionToInt

    totalInversion = totalInversionFrom + totalInversionTo

    try:
        saldoSQL()
    except sqlite3.Error:
        totalInversion = 0
        valorActual = 0
        dif = 0
        error_base_datos = "ERROR EN LA BASE DE DATOS"
        return render_template("status.html", menu = 'status', error_base_datos = error_base_datos, noHayMovimiento = True)

    xi = 0
    cryptoValorActual = {}
    valorActual = 0
    for moneda in cryptos:
        consultaApi = api(moneda, 'EUR')
        if consultaApi[0] =='error':
            totalInversion = 0
            valorActual = 0
            dif = 0
            mensajeError = errorApi(consultaApi[1])
            errorAPI = "ERROR EN LA API - {}".format(mensajeError)
            return render_template("status.html", menu = 'status', errorAPI = errorAPI, totalInversion=totalInversion, cryptoBalance=saldoSQL(), valorActual=valorActual, dif = dif)
        else:
            cotizacion = consultaApi[1]
            saldoMoneda = saldoSQL()[xi]
            cryptoValorActual[moneda] = cotizacion * saldoMoneda
            valorActual -= cryptoValorActual[moneda]
            xi += 1

    dif = valorActual - totalInversion

    return render_template("status.html", menu = 'status', totalInversion=totalInversion, valorActual=valorActual, dif = dif, cryptoBalance=saldoSQL())
