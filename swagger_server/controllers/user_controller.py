import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.user_with_out_id import UserWithOutId  # noqa: E501
from swagger_server.models.user_with_out_password import UserWithOutPassword  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: UserWithOutPassword
    """
    if connexion.request.is_json:
        body = UserWithOutId.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_users_with_list_input(body):  # noqa: E501
    """Creates list of users with given an array

     # noqa: E501

    :param body: List of user object
    :type body: list | bytes

    :rtype: List[UserWithOutPassword]
    """
    if connexion.request.is_json:
        body = [UserWithOutId.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_user(id):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_my_user():  # noqa: E501
    """Get user by user token

     # noqa: E501


    :rtype: UserWithOutPassword
    """
    return 'do some magic!'


def get_one_user(id):  # noqa: E501
    """Get user by user id

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: UserWithOutPassword
    """
    return 'do some magic!'


def list_users():  # noqa: E501
    """List all users

     # noqa: E501


    :rtype: List[UserWithOutPassword]
    """
    return 'do some magic!'


def update_user(id, body):  # noqa: E501
    """Updated user

    This can only be done by the logged in user. # noqa: E501

    :param id: name that need to be updated
    :type id: str
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: UserWithOutPassword
    """
    if connexion.request.is_json:
        body = UserWithOutId.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
