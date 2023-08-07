from peewee import SqliteDatabase
db = SqliteDatabase('oltp.db')

def create_tables():
    from app.models.Usuario import Usuario
    from app.models.Cuenta import Cuenta
    from app.models.Tarjeta import Tarjeta
    db.connect()
    db.create_tables([Usuario, Cuenta, Tarjeta])