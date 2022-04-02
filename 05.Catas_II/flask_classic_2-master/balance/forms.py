from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.fields.core import DateField, RadioField, StringField, FloatField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class MovimientoFormulario(FlaskForm):
    fecha = DateField("Fecha", validators=[DataRequired(message="Debe informar la fecha")])
    concepto = StringField("Concepto", validators=[DataRequired(message="Debe informar del concepto"), Length(min=10)])
    cantidad = FloatField("Cantidad", validators=[DataRequired(message="Debe informar el monto del movimiento"),
                                                    NumberRange(message="Debe informar un importe positivo", min=0.01)])
    ingreso_gasto = RadioField(validators=[DataRequired(message="Debe informar el tipo de movimiento")],
                                            choices=[(0, "Gasto"), (1, "Ingreso")])

    submit = SubmitField("Aceptar")

