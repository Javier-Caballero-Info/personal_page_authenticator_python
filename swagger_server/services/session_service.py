from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class SessionService:

    @staticmethod
    def authenticate(credential):

        if credential.username == 'admin' and credential.password == 'admin':
            access_token = create_access_token(identity=credential.username)
            refresh_token = create_refresh_token(identity=credential.username)
            return {
                    'message': 'Logged in as {}'.format(credential.username),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
        else:
            return None

    @staticmethod
    def renew_token(identity):

        access_token = create_access_token(identity=identity)

        return {
            'message': 'Logged in as {}'.format(identity),
            'access_token': access_token
        }
