from peewee import CharField
from ..models.Base import BaseModel

class Usuario(BaseModel):
    nombre = CharField()
    # Other user fields
    