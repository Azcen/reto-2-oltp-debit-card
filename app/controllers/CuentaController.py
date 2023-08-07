from ..models.Cuenta import Cuenta

def crear_cuenta(usuario, saldo):
    return Cuenta.create(usuario=usuario, saldo=saldo)

def obtener_cuentas_usuario(usuario):
    return Cuenta.select().where(Cuenta.usuario == usuario)

  
def actualizar_saldo_cuenta(cuenta):
  saldo = sum([tarjeta.balance for tarjeta in cuenta.tarjetas])
  cuenta.saldo = saldo
  cuenta.save()

def eliminar_cuenta(cuenta):
    cuenta.delete_instance()