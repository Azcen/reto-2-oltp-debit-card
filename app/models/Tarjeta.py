from peewee import ForeignKeyField, DecimalField
from ..models.Base import BaseModel
from ..models.Cuenta import Cuenta

class Tarjeta(BaseModel):
    cuenta = ForeignKeyField(Cuenta, backref='tarjetas')
    balance = DecimalField()

    def procesar_deposito(self, monto):
        self.balance += monto
        self.save()

    def procesar_gasto(self, monto):
        if self.balance >= monto:
            self.balance -= monto
            self.save()
        else:
            raise ValueError("Saldo insuficiente para procesar el gasto")