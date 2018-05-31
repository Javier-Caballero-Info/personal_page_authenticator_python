import connexion
import jsonschema
from flask_api import status
from flask_jwt_extended import jwt_required, get_jwt_identity

from swagger_server.models import User, ApiResponse
from swagger_server.models.password import Password
from swagger_server.utils.schema_validator import SchemaValidator
from swagger_server.services.user_service import UserService
from swagger_server.utils.response_helper import ResponseHelper


@jwt_required
def create_user():
    try:

        if connexion.request.is_json:

            SchemaValidator.validate_user_schema(connexion.request.get_json())

            body = User.from_dict(connexion.request.get_json())

            other_user = UserService.get_by_username(body.username)

            if other_user is None:

                result = UserService.create(body)

                if result is not None:
                    return ResponseHelper.response_201(result.to_json())
                else:
                    return ResponseHelper.response_400('Something went wrong')
            else:
                return ResponseHelper.response_400('Username already taken')

    except jsonschema.exceptions.ValidationError as e:
        return ResponseHelper.response_400(e.message)


@jwt_required
def create_users_with_list_input():

    if connexion.request.is_json:

        users = [User.from_dict(d) for d in connexion.request.get_json()]

        result = []

        for u in users:
            try:
                SchemaValidator.validate_user_schema(u.to_json(show_id=False, show_password=True))
                other_user = UserService.get_by_username(u.username)

                if other_user is None:

                    new_user = UserService.create(u)

                    if result is not None:
                        result.append(ApiResponse(
                            status.HTTP_200_OK,
                            'Ok',
                            new_user.id
                        ))
                    else:
                        result.append(ApiResponse(
                            status.HTTP_400_BAD_REQUEST,
                            'BAD_REQUEST',
                            'Something went wrong'
                        ))
                else:
                    result.append(ApiResponse(
                        status.HTTP_400_BAD_REQUEST,
                        'BAD_REQUEST',
                        'Username already taken'
                    ))
            except jsonschema.exceptions.ValidationError as e:
                result.append(ApiResponse(
                    status.HTTP_400_BAD_REQUEST,
                    'BAD_REQUEST',
                    e.message
                ))

        return ResponseHelper.response_200(result)


@jwt_required
def delete_user(id):

    result = UserService.get_by_id(id)

    if result is not None:
        if len(UserService.get_all()) > 1:
            UserService.remove(id)
            return ResponseHelper.response_204()
        else:
            return ResponseHelper.response_406('Must exists at least one user')
    else:
        return ResponseHelper.response_404('User not found')


@jwt_required
def change_password():
    try:

        if connexion.request.is_json:

            SchemaValidator.validate_password_schema(connexion.request.get_json())

            body = Password.from_dict(connexion.request.get_json())

            if body.password == body.password_confirmation:

                result = UserService.change_password(get_jwt_identity(), body.password)

                if result is not None:
                    return ResponseHelper.response_204()
                else:
                    return ResponseHelper.response_400('Something went wrong')
            else:
                return ResponseHelper.response_400("Passwords don't match")

    except jsonschema.exceptions.ValidationError as e:
        return ResponseHelper.response_400(e.message)


@jwt_required
def get_my_user():
    result = UserService.get_by_id(get_jwt_identity())

    if result is not None:
        return ResponseHelper.response_200(result.to_json())
    else:
        return ResponseHelper.response_404('User not found')


@jwt_required
def get_one_user(id):
    result = UserService.get_by_id(id)

    if result is not None:
        return ResponseHelper.response_200(result.to_json())
    else:
        return ResponseHelper.response_404('User not found')


@jwt_required
def list_users():

    return ResponseHelper.response_200(list(map(lambda x: x.to_json(), UserService.get_all())))


@jwt_required
def update_user(id):
    try:

        if connexion.request.is_json:

            SchemaValidator.validate_user_schema(connexion.request.get_json())

            body = User.from_dict(connexion.request.get_json())

            other_user = UserService.get_by_username(body.username)

            if other_user is None or other_user.id == id:

                result = UserService.edit(id, body)

                if result is not None:
                    return ResponseHelper.response_200(result.to_json())
                else:
                    return ResponseHelper.response_404('User not found')
            else:
                return ResponseHelper.response_400('Username already taken')

    except jsonschema.exceptions.ValidationError as e:
        return ResponseHelper.response_400(e.message)
