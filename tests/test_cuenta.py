import pytest
from peewee import SqliteDatabase
from app.controllers.CuentaController import crear_cuenta, obtener_cuentas_usuario, actualizar_saldo_cuenta, eliminar_cuenta
from app.models.Usuario import Usuario
from app.models.Cuenta import Cuenta
from app.models.Tarjeta import Tarjeta

db_test = SqliteDatabase(':memory:')

@pytest.fixture(scope='function')
def setup_db():
    Tarjeta._meta.database = db_test
    Cuenta._meta.database = db_test
    Usuario._meta.database = db_test
    db_test.connect()
    db_test.create_tables([Usuario, Cuenta, Tarjeta])
    
    with db_test.atomic():
        usuario = Usuario.create(nombre='Juan')
        
        cuenta = Cuenta.create(usuario=usuario, saldo=1000.00)
        
        Tarjeta.create(cuenta=cuenta, balance=500.00)
        yield cuenta
    
    db_test.drop_tables([Usuario, Cuenta, Tarjeta])
    db_test.close()

def test_crear_cuenta(setup_db):
    usuario = Usuario.create(nombre='Juan')
    cuenta = crear_cuenta(usuario, saldo=1000.00)
    assert cuenta.saldo == 1000.00

def test_obtener_cuentas_usuario(setup_db):
    usuario = Usuario.create(nombre='Juan')
    cuenta1 = crear_cuenta(usuario, saldo=1000.00)
    cuenta2 = crear_cuenta(usuario, saldo=2000.00)
    
    cuentas = obtener_cuentas_usuario(usuario)
    assert len(cuentas) == 2
    assert cuentas[0].saldo == 1000.00
    assert cuentas[1].saldo == 2000.00

def test_actualizar_saldo_cuenta(setup_db):
    usuario = Usuario.create(nombre='Juan')
    cuenta = crear_cuenta(usuario, saldo=1000.00)
    
    Tarjeta.create(cuenta=cuenta, balance=500.00)
    Tarjeta.create(cuenta=cuenta, balance=300.00)
    
    actualizar_saldo_cuenta(cuenta)
    assert cuenta.saldo == 800.00

def test_eliminar_cuenta(setup_db):
    cuenta = setup_db
    eliminar_cuenta(cuenta)
    
    cuentas = obtener_cuentas_usuario(cuenta.usuario)
    assert len(cuentas) == 0
