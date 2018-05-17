#!/usr/bin/env python3

import connexion

from swagger_server.utils.encoder import JSONEncoder
from flask_jwt_extended import JWTManager

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Authetication Server for Personal Page Admin'})
    app.app.config['SECRET_KEY'] = 'some-secret-string'
    app.app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

    jwt = JWTManager(app.app)

    app.run(port=3000, debug=True)


if __name__ == '__main__':
    main()
