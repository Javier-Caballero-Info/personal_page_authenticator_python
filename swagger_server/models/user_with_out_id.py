# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserWithOutId(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, username: str=None, first_name: str=None, last_name: str=None, email: str=None, password: str=None):  # noqa: E501
        """UserWithOutId - a model defined in Swagger

        :param username: The username of this UserWithOutId.  # noqa: E501
        :type username: str
        :param first_name: The first_name of this UserWithOutId.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this UserWithOutId.  # noqa: E501
        :type last_name: str
        :param email: The email of this UserWithOutId.  # noqa: E501
        :type email: str
        :param password: The password of this UserWithOutId.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'username': str,
            'first_name': str,
            'last_name': str,
            'email': str,
            'password': str
        }

        self.attribute_map = {
            'username': 'username',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'password': 'password'
        }

        self._username = username
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'UserWithOutId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserWithOutId of this UserWithOutId.  # noqa: E501
        :rtype: UserWithOutId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this UserWithOutId.


        :return: The username of this UserWithOutId.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this UserWithOutId.


        :param username: The username of this UserWithOutId.
        :type username: str
        """

        self._username = username

    @property
    def first_name(self) -> str:
        """Gets the first_name of this UserWithOutId.


        :return: The first_name of this UserWithOutId.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this UserWithOutId.


        :param first_name: The first_name of this UserWithOutId.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this UserWithOutId.


        :return: The last_name of this UserWithOutId.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this UserWithOutId.


        :param last_name: The last_name of this UserWithOutId.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def email(self) -> str:
        """Gets the email of this UserWithOutId.


        :return: The email of this UserWithOutId.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserWithOutId.


        :param email: The email of this UserWithOutId.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this UserWithOutId.


        :return: The password of this UserWithOutId.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this UserWithOutId.


        :param password: The password of this UserWithOutId.
        :type password: str
        """

        self._password = password
