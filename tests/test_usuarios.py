import pytest
from peewee import SqliteDatabase
from app.models.Usuario import Usuario
from app.controllers.UserController import crear_usuario, obtener_usuarios, actualizar_usuario, eliminar_usuario

# Utilidad para configurar una base de datos de prueba en memoria
db_test = SqliteDatabase(':memory:')

@pytest.fixture(scope='function')
def setup_db():
    # Conectar la base de datos de prueba
    Usuario._meta.database = db_test
    db_test.connect()
    db_test.create_tables([Usuario])
    yield
    db_test.drop_tables([Usuario])
    db_test.close()

def test_crear_usuario(setup_db):
    usuario = crear_usuario('Juan')
    assert usuario.nombre == 'Juan'
    
def test_obtener_usuarios(setup_db):
    crear_usuario('Juan')
    crear_usuario('Maria')
    
    usuarios = obtener_usuarios()
    assert len(usuarios) == 2
    assert usuarios[0].nombre == 'Juan'
    assert usuarios[1].nombre == 'Maria'
    
def test_actualizar_usuario(setup_db):
    usuario = crear_usuario('Juan')
    actualizar_usuario(usuario, 'Pedro')
    usuario_actualizado = Usuario.get(Usuario.id == usuario.id)
    assert usuario_actualizado.nombre == 'Pedro'
    
def test_eliminar_usuario(setup_db):
    usuario = crear_usuario('Juan')
    eliminar_usuario(usuario)
    usuarios = obtener_usuarios()
    assert len(usuarios) == 0
