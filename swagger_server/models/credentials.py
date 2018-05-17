# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Credentials(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, username: str=None, password: str=None):  # noqa: E501
        """Credentials - a model defined in Swagger

        :param username: The username of this Credentials.  # noqa: E501
        :type username: str
        :param password: The password of this Credentials.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'username': str,
            'password': str
        }

        self.attribute_map = {
            'username': 'username',
            'password': 'password'
        }

        self._username = username
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'Credentials':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Credentials of this Credentials.  # noqa: E501
        :rtype: Credentials
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this Credentials.


        :return: The username of this Credentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this Credentials.


        :param username: The username of this Credentials.
        :type username: str
        """

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this Credentials.


        :return: The password of this Credentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this Credentials.


        :param password: The password of this Credentials.
        :type password: str
        """

        self._password = password
