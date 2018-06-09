import connexion
import jsonschema
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity

from swagger_server.models.credentials import Credentials
from swagger_server.services.session_service import SessionService
from swagger_server.utils.response_helper import ResponseHelper
from swagger_server.utils.schema_validator import SchemaValidator


def create_session():
    try:

        if connexion.request.is_json:

            SchemaValidator.validate_credential_schema(connexion.request.get_json())

            body = Credentials.from_dict(connexion.request.get_json())

            token = SessionService.authenticate(body)

            if token is not None:
                return ResponseHelper.response_201(token)
            else:
                return ResponseHelper.response_400('Wrong credentials')

    except jsonschema.exceptions.ValidationError as e:
        return ResponseHelper.response_400('Wrong credentials')


@jwt_refresh_token_required
def update_session():
    try:

        return SessionService.renew_token(get_jwt_identity())

    except KeyError:

        return ResponseHelper.response_400('Missing refresh token')
