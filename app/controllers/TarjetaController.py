from ..models.Tarjeta import Tarjeta

def crear_tarjeta(cuenta, balance):
    return Tarjeta.create(cuenta=cuenta, balance=balance)
  
def obtener_tarjetas_cuenta(cuenta):
    return Tarjeta.select().where(Tarjeta.cuenta == cuenta)

def procesar_deposito_tarjeta(tarjeta, monto):
    tarjeta.balance += monto
    tarjeta.save()

def procesar_gasto_tarjeta(tarjeta, monto):
    if tarjeta.balance >= monto:
        tarjeta.balance -= monto
        tarjeta.save()
    else:
        raise ValueError("Saldo insuficiente para procesar el gasto")

def eliminar_tarjeta(tarjeta):
    tarjeta.delete_instance()
