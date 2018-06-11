import jsonschema
import simplejson as json


class SchemaValidator(object):

    @staticmethod
    def _get_schema(schema_name):
        with open('./swagger_server/schemas/%s.json' % schema_name, 'r') as f:
            schema_data = f.read()

        return json.loads(schema_data)

    @staticmethod
    def validate_credential_schema(data):
        schema = SchemaValidator._get_schema('credential')

        return jsonschema.validate(data, schema)

    @staticmethod
    def validate_create_user_schema(data):
        schema = SchemaValidator._get_schema('create_user')

        return jsonschema.validate(data, schema)

    @staticmethod
    def validate_edit_user_schema(data):
        schema = SchemaValidator._get_schema('edit_user')

        return jsonschema.validate(data, schema)

    @staticmethod
    def validate_password_schema(data):
        schema = SchemaValidator._get_schema('password')

        return jsonschema.validate(data, schema)
