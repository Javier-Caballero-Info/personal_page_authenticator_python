# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.user_with_out_id import UserWithOutId  # noqa: E501
from swagger_server.models.user_with_out_password import UserWithOutPassword  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""
    pass


if __name__ == '__main__':
    import unittest
    unittest.main()
