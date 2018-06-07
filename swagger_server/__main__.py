#!/usr/bin/env python3

import connexion
from swagger_server.services import db
from swagger_server.utils.encoder import JSONEncoder
from flask_jwt_extended import JWTManager

from flask_cors import CORS
import os


def main():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Authentication Server for Personal Page Admin'})

    try:
        secret_key = os.environ['SECRET_KEY']
    except KeyError:
        secret_key = 'some-secret-string'

    app.app.config['SECRET_KEY'] = secret_key

    try:
        jwt_secret_key = os.environ['JWT_SECRET_KEY']
    except KeyError:
        jwt_secret_key = 'jwt-secret-string'

    app.app.config['JWT_SECRET_KEY'] = jwt_secret_key

    try:
        jwt_algorithm = os.environ['JWT_SIGN_ALGORITHM']
    except KeyError:
        jwt_algorithm = 'HS384'

    app.app.config['JWT_ALGORITHM'] = jwt_algorithm

    JWTManager(app.app)

    CORS(app.app)

    db.init_app(app.app)

    try:
        port = os.environ['PORT']
    except KeyError:
        port = 3000

    app.run(port=port)


if __name__ == '__main__':
    main()
