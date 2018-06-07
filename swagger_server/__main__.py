#!/usr/bin/env python3

import connexion
import os

from swagger_server.services import db
from swagger_server.utils.encoder import JSONEncoder
from flask_jwt_extended import JWTManager

from flask_cors import CORS


def main():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Authentication Server for Personal Page Admin'})
    app.app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
    app.app.config['JWT_ALGORITHM'] = os.environ['JWT_SIGN_ALGORITHM']

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
