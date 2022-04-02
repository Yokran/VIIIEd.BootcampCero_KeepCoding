from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import InputRequired, NumberRange

class CompraFormulario(FlaskForm):
    from_moneda = SelectField('From', choices=[('EUR', 'EUR - EURO'), ('BTC', 'BTC - Bitcoin'), ('ETH', 'ETH - Ether'), ('XRP', 'XRP - Ripple'), ('LTC', 'LTC - Litecoin'), ('BCH', 'BCH - Bitcoin Cash'), ('BNB', 'BNB - Binance Coin'), ('USDT', 'USDT - Tether'), ('EOS', 'EOS - EOS'), ('BSV', 'BSV - Bitcoin SV'), ('XLM', 'XLM - Stellar'), ('ADA', 'ADA - Cardano'), ('TRX', 'TRX - TRON')])
    to_moneda = SelectField('To', choices=[('EUR', 'EUR - EURO'), ('BTC', 'BTC - Bitcoin'), ('ETH', 'ETH - Ether'), ('XRP', 'XRP - Ripple'), ('LTC', 'LTC - Litecoin'), ('BCH', 'BCH - Bitcoin Cash'), ('BNB', 'BNB - Binance Coin'), ('USDT', 'USDT - Tether'), ('EOS', 'EOS - EOS'), ('BSV', 'BSV - Bitcoin SV'), ('XLM', 'XLM - Stellar'), ('ADA', 'ADA - Cardano'), ('TRX', 'TRX - TRON')])
    to_cantidad = FloatField('Cantidad', validators=[InputRequired(), NumberRange(min=0.00001, max=99999999)])

    submitCalcular = SubmitField('Calcular')
    submitAceptar = SubmitField('Aceptar')
