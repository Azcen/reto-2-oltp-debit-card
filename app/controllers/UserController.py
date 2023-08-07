from ..models.Usuario import Usuario

def crear_usuario(nombre):
    return Usuario.create(nombre=nombre)
  
def obtener_usuarios():
    return Usuario.select()
  
def actualizar_usuario(usuario, nuevo_nombre):
    usuario.nombre = nuevo_nombre
    usuario.save()
    
def eliminar_usuario(usuario):
    usuario.delete_instance()