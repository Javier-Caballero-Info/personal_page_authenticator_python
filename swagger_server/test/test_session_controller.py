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

    def test_create_session(self):
        """Test case for create_session

        Create Session
        """
        body = Credentials()
        response = self.client.open(
            '/v1/session',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_session(self):
        """Test case for update_session

        Update Session
        """
        response = self.client.open(
            '/v1/session',
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
