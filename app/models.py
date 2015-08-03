from peewee import *

from app import db

DATABASE = SqliteDatabase('coremi.db')

class Usuario(Model):
    usuario = CharField(null=False, unique=True)
    password = CharField(null=False, max_length=100)
    nombreuno = CharField(null=False)
    nombredos = CharField()
    nombretres = CharField()
    apepaterno = CharField(null=False)
    apematerno = CharField()
    sexo = FixedCharField(max_length=1)
    fechanacimiento = DateField()
    administrador = BooleanField(default=False)
    fechacreacion = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
    
    @classmethod
    def crear_usuario(cls, ):
        pass

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Usuario], safe+True)
    DATABASE.close()