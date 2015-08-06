from flask import Flask, g, jsonify
from flask_restful import Api

import models
import resources

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def custom_error_404(error):
    response = jsonify({'message': error.description})
    return response
    
@app.errorhandler(500)
def custom_error_500(error):
    response = jsonify({'message': error.description})
    return response

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"


api.add_resource(resources.ResourceUsuario, '/coremi/api/usuarios/<usuario>')
api.add_resource(resources.ResourceUsuarioLista, '/coremi/api/usuarios')
api.add_resource(resources.ResourceLogin, '/coremi/api/login')


if __name__ == '__main__':
    models.initialize()
    try:
        models.Usuario.crear_usuario(
                nombreusuario='ramijtc@gmail.com',
                password='password',
                nombreuno='Ramiro',
                nombredos='Jhonatan',
                nombretres=None,
                apepaterno='Torrejon',
                apematerno='Castro',
                sexo='M',
                fechanacimiento='2015-01-04',
                administrador=True
            )
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)