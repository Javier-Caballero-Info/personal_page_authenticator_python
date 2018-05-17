import jsonschema
import simplejson as json

class SchemaValidator(object):

	@staticmethod
	def _get_schema(schema_name):
		with open('./swagger_server/schemas/%s.json' % schema_name, 'r') as f:
		    schema_data = f.read()
			
		return json.loads(schema_data)

	@staticmethod
	def validateCredentialSchema(data):
		schema = SchemaValidator._get_schema('credentials')

		return jsonschema.validate(data, schema)