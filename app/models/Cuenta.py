from peewee import ForeignKeyField, DecimalField
from ..models.Base import BaseModel
from ..models.Usuario import Usuario

class Cuenta(BaseModel):
    usuario = ForeignKeyField(Usuario, backref='cuentas')
    saldo = DecimalField()