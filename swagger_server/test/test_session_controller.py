# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.access_token_refreshed import AccessTokenRefreshed  # noqa: E501
from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.credentials import Credentials  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSessionController(BaseTestCase):
    """SessionController integration test stubs"""

    pass


if __name__ == '__main__':
    import unittest
    unittest.main()
