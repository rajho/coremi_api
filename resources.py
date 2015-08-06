from flask import abort
from flask.ext.bcrypt import check_password_hash
from flask_restful import Resource, reqparse

import models


class ResourceUsuario(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('nombreusuario', type=str, required=True, 
                                   help='nombreusuario no enviado', location='json')
        self.reqparse.add_argument('password', type=str, required=True, 
                                   help='password no enviado', location='json')
        self.reqparse.add_argument('nombreuno', type=str, required=True, 
                                   help='nombreuno no enviado', location='json')
        self.reqparse.add_argument('nombredos', type=str, location='json')
        self.reqparse.add_argument('nombretres', type=str, location='json')
        self.reqparse.add_argument('apepaterno', type=str, required=True, 
                                   help='apepaterno no enviado', location='json')
        self.reqparse.add_argument('apematerno', type=str, location='json')
        self.reqparse.add_argument('sexo', type=str, location='json')
        self.reqparse.add_argument('fechanacimiento', type=str, location='json')
        self.reqparse.add_argument('administrador', type=str, location='json')
        super(ResourceUsuario, self).__init__()
    
    def get(self, usuario):
        print("Usuario: {0}".format(usuario))
        usuario = models.Usuario.select().where(models.Usuario.nombreusuario == usuario)
        res = {'usuarios':[]}
        for u in usuario:
            res['usuarios'].append({'id': u.id,
                                    'usuario': u.nombreusuario, 
                                    'nombre': u.nombreuno,
                                    'apepaterno': u.apepaterno})
        return res
    
    def put(self, usuario):
        args = self.reqparse.parse_args()
        admin = True if args['administrador'] == 'True' else False
        try:
            models.Usuario.crear_usuario(
                nombreusuario=args['nombreusuario'],
                password=args['password'],
                nombreuno=args['nombreuno'],
                nombredos=args['nombredos'],
                nombretres=args['nombretres'],
                apepaterno=args['apepaterno'],
                apematerno=args['apematerno'],
                sexo=args['sexo'],
                fechanacimiento=args['fechanacimiento'],
                administrador=admin
            )
        except ValueError as e:
            abort(500, 'Error al crear usuario')
        return args['nombreuno'], 201
        
    def delete(self, usuario):
        pass


class ResourceUsuarioLista(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('nombreusuario', type=str, required=True, 
                                   help='nombreusuario no enviado', location='json')
        self.reqparse.add_argument('password', type=str, required=True, 
                                   help='password no enviado', location='json')
        self.reqparse.add_argument('nombreuno', type=str, required=True, 
                                   help='nombreuno no enviado', location='json')
        self.reqparse.add_argument('nombredos', type=str, location='json')
        self.reqparse.add_argument('nombretres', type=str, location='json')
        self.reqparse.add_argument('apepaterno', type=str, required=True, 
                                   help='apepaterno no enviado', location='json')
        self.reqparse.add_argument('apematerno', type=str, location='json')
        self.reqparse.add_argument('sexo', type=str, location='json')
        self.reqparse.add_argument('fechanacimiento', type=str, location='json')
        self.reqparse.add_argument('administrador', type=str, location='json')
        super(ResourceUsuarioLista, self).__init__()
    
    def get(self):
        usuarios = models.Usuario.select().limit(100)
        res = {'usuarios':[]}
        for u in usuarios:
            res['usuarios'].append({'id': u.id,
                                    'usuario': u.nombreusuario, 
                                    'nombre': u.nombreuno,
                                    'apepaterno': u.apepaterno})
        return res
    
    def post(self):
        args = self.reqparse.parse_args()
        admin = True if args['administrador'] == 'True' else False
        try:
            models.Usuario.crear_usuario(
                nombreusuario=args['nombreusuario'],
                password=args['password'],
                nombreuno=args['nombreuno'],
                nombredos=args['nombredos'],
                nombretres=args['nombretres'],
                apepaterno=args['apepaterno'],
                apematerno=args['apematerno'],
                sexo=args['sexo'],
                fechanacimiento=args['fechanacimiento'],
                administrador=admin
            )
        except ValueError as e:
            abort(500, 'Error al crear usuario')
        return args['nombreuno'], 201
        
        
class ResourceLogin(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('nombreusuario', type=str, required=True, 
                                   help='nombreusuario no enviado', location='json')
        self.reqparse.add_argument('password', type=str, required=True, 
                                   help='password no enviado', location='json')
        super(ResourceLogin, self).__init__()
        
    def post(self):
        args = self.reqparse.parse_args()
        res = {'sucess':'True', 'statusCode': 200, 'reason': ''}
        try:
            usuario = models.Usuario.get(models.Usuario.nombreusuario == args['nombreusuario'])
        except models.DoesNotExist:
            res['reason'] = 'Usuario con email: {0} - no existe'.format(args['nombreusuario'])
            res['logged'] = "False"
            res['statusCode'] = 500
            return res, 500
        else:
            if check_password_hash(usuario.password, args['password']):
                res['reason'] = "Usuario logueado."
                res['logged'] = "True"
                return res, 200
            else:
                res['statusCode'] = 500
                res['reason'] = "Usuario o clave incorrecta."
                res['logged'] = "False"
                return res, 500
            