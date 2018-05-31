from flask import jsonify, request
from flask_api import status, exceptions
from swagger_server.models.api_response import ApiResponse


class ResponseHelper:

    @staticmethod
    def response_200(response):
        return response, status.HTTP_200_OK

    @staticmethod
    def response_201(response):
        return response, status.HTTP_201_CREATED

    @staticmethod
    def response_204():
        return {}, status.HTTP_204_NO_CONTENT

    @staticmethod
    def response_404(message):
        api_response = ApiResponse(
            status.HTTP_404_NOT_FOUND,
            'NOT_FOUND',
            message
        )

        return api_response, status.HTTP_404_NOT_FOUND

    @staticmethod
    def response_400(message):
        api_response = ApiResponse(
            status.HTTP_400_BAD_REQUEST,
            'BAD_REQUEST',
            message
        )

        return api_response, status.HTTP_400_BAD_REQUEST

    @staticmethod
    def response_406(message):
        api_response = ApiResponse(
            status.HTTP_400_BAD_REQUEST,
            'BAD_REQUEST',
            message
        )

        return api_response, status.HTTP_406_NOT_ACCEPTABLE
