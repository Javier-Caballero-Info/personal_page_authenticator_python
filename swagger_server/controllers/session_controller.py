import connexion
import six
import jsonschema
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.access_token_refreshed import AccessTokenRefreshed  # noqa: E501
from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.credentials import Credentials  # noqa: E501
from swagger_server import util
from swagger_server.services.session_service import SessionService
from swagger_server.utils.response_helper import ResponseHelper
from swagger_server.utils.schema_validator import SchemaValidator


def create_session():  # noqa: E501
    """Create Session

     # noqa: E501

    :param body: Created a session
    :type body: dict | bytes

    :rtype: AccessToken
    """

    try:

        if connexion.request.is_json:

            SchemaValidator.validateCredentialSchema(connexion.request.get_json())

            body = Credentials.from_dict(connexion.request.get_json())

            token = SessionService.authenticate(body)

            if token is not None:
                return ResponseHelper.response_201(token)
            else:
                return ResponseHelper.response_400('Wrong credentials')

    except jsonschema.exceptions.ValidationError as e:
        print(e)
        return ResponseHelper.response_400('Wrong credentials')


@jwt_refresh_token_required
def update_session():  # noqa: E501
    """Update Session

     # noqa: E501


    :rtype: AccessTokenRefreshed
    """

    try:

        return SessionService.renew_token(get_jwt_identity())

    except KeyError:

        return ResponseHelper.response_400('Missing refresh token')
