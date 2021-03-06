from flask_jwt_extended import (create_access_token, create_refresh_token)

from swagger_server.models import User
from swagger_server.services.user_service import UserService


class SessionService:

    @staticmethod
    def authenticate(credential):

        user: User = UserService.get_by_username(credential.username)

        if user is not None and user.check_password(credential.password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return {
                    'message': 'Logged in as {}'.format(user.username),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
        else:
            return None

    @staticmethod
    def renew_token(identity):

        access_token = create_access_token(identity=identity)

        user: User = UserService.get_by_id(identity)

        return {
            'message': 'Logged in as {}'.format(user.username),
            'access_token': access_token
        }
