import pytest
from peewee import SqliteDatabase
from app.controllers.TarjetaController import crear_tarjeta, obtener_tarjetas_cuenta, procesar_deposito_tarjeta, procesar_gasto_tarjeta, eliminar_tarjeta
from app.models.Usuario import Usuario
from app.models.Cuenta import Cuenta
from app.models.Tarjeta import Tarjeta

# Utilidad para configurar una base de datos de prueba en memoria
db_test = SqliteDatabase(':memory:')

@pytest.fixture(scope='function')
def setup_db():
    # Conectar la base de datos de prueba
    Tarjeta._meta.database = db_test
    Cuenta._meta.database = db_test
    Usuario._meta.database = db_test
    db_test.connect()
    db_test.create_tables([Usuario, Cuenta, Tarjeta])
    
    with db_test.atomic():
        # Crear un usuario
        usuario = Usuario.create(nombre='Juan')
        
        # Crear una cuenta para las pruebas
        cuenta = Cuenta.create(usuario=usuario, saldo=1000.00)
        yield cuenta
    
    db_test.drop_tables([Usuario, Cuenta, Tarjeta])
    db_test.close()

def test_crear_tarjeta(setup_db):
    cuenta = setup_db
    tarjeta = crear_tarjeta(cuenta, balance=1000.00)
    assert tarjeta.balance == 1000.00

def test_obtener_tarjetas_cuenta(setup_db):
    cuenta = setup_db
    tarjeta1 = crear_tarjeta(cuenta, balance=1000.00)
    tarjeta2 = crear_tarjeta(cuenta, balance=2000.00)
    
    tarjetas = obtener_tarjetas_cuenta(cuenta)
    assert len(tarjetas) == 2
    assert tarjetas[0].balance == 1000.00
    assert tarjetas[1].balance == 2000.00

def test_procesar_deposito_tarjeta(setup_db):
    cuenta = setup_db
    tarjeta = crear_tarjeta(cuenta, balance=1000.00)
    
    procesar_deposito_tarjeta(tarjeta, monto=500.00)
    assert tarjeta.balance == 1500.00

def test_procesar_gasto_tarjeta(setup_db):
    cuenta = setup_db
    tarjeta = crear_tarjeta(cuenta, balance=1000.00)
    
    procesar_gasto_tarjeta(tarjeta, monto=700.00)
    assert tarjeta.balance == 300.00
    
    with pytest.raises(ValueError):
        procesar_gasto_tarjeta(tarjeta, monto=500.00)

def test_eliminar_tarjeta(setup_db):
    cuenta = setup_db
    tarjeta = crear_tarjeta(cuenta, balance=1000.00)
    eliminar_tarjeta(tarjeta)
    
    tarjetas = obtener_tarjetas_cuenta(cuenta)
    assert len(tarjetas) == 0
