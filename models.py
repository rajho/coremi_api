import datetime

from flask.ext.bcrypt import generate_password_hash
from peewee import *

DATABASE = SqliteDatabase('coremi.db')

class Usuario(Model):
    nombreusuario = CharField(unique=True)
    password = CharField(max_length=100)
    nombreuno = CharField()
    nombredos = CharField(null=True)
    nombretres = CharField(null=True)
    apepaterno = CharField()
    apematerno = CharField(null=True)
    sexo = FixedCharField(max_length=1, null=True)
    fechanacimiento = DateField(null=True)
    administrador = BooleanField(default=False)
    fechacreacion = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
    
    @classmethod
    def crear_usuario(cls, nombreusuario, password, nombreuno, nombredos, nombretres, 
                      apepaterno, apematerno, sexo, fechanacimiento, administrador=False):
        try:
            with DATABASE.transaction():
                cls.create(
                    nombreusuario=nombreusuario,
                    password=generate_password_hash(password),
                    nombreuno=nombreuno,
                    nombredos=nombredos,
                    nombretres=nombretres,
                    apepaterno=apepaterno,
                    apematerno=apematerno,
                    sexo=sexo,
                    fechanacimiento=fechanacimiento,
                    administrador=administrador)
        except IntegrityError as e:
            raise ValueError("Error al crear Usuario :M" + str(e))


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Usuario], safe=True)
    DATABASE.close()