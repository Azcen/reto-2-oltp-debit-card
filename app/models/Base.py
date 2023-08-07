from peewee import Model
from ..db.dbConn import db
class BaseModel(Model):
    class Meta:
        database = db