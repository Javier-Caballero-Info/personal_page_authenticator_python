#!/usr/bin/env python3

import connexion

from swagger_server.utils.encoder import JSONEncoder
from flask_jwt_extended import JWTManager

from flask_cors import CORS


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Authentication Server for Personal Page Admin'})
    app.app.config['SECRET_KEY'] = 'some-secret-string'
    app.app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    app.app.config['JWT_ALGORITHM'] = 'HS384'

    JWTManager(app.app)

    CORS(app.app)

    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
