import connexion
import six
import jsonschema

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.access_token_refreshed import AccessTokenRefreshed  # noqa: E501
from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.credentials import Credentials  # noqa: E501
from swagger_server import util
from swagger_server.services.session_service import SessionService
from swagger_server.utils.response_helper import ResponseHelper
from swagger_server.utils.schema_validator import SchemaValidator


def create_session(body):  # noqa: E501
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

            if token != None:
                return ResponseHelper.response_201(token)
            else:
                return ResponseHelper.response_400('Wrong credentials')

    except jsonschema.exceptions.ValidationError as e:
        print(e)
        return ResponseHelper.response_400('Wrong credentials')

def update_session():  # noqa: E501
    """Update Session

     # noqa: E501


    :rtype: AccessTokenRefreshed
    """
    return 'do some magic!'
