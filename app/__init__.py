from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from app.config import get_config
from app.routes	import blueprints
from app.extension import cors

app = Flask(__name__)

def init_extensions():
	cors.init_app(app)


def init_swagger():
	SWAGGER_URL = '/api/docs'
	API_URL = 'swagger.json'

	@app.route('/api/docs/swagger.json')
	def serve_swagger_json():
		with open('./app/docs/swagger.json', 'r') as f:
			swagger_json = f.read()
		return swagger_json


	swagger = get_swaggerui_blueprint(
		SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
		API_URL,
		config={  # Swagger UI config overrides
			# 'app_name': "Test application"
		},
		# oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
		#    'clientId': "your-client-id",
		#    'clientSecret': "your-client-secret-if-required",
		#    'realm': "your-realms",
		#    'appName': "your-app-name",
		#    'scopeSeparator': " ",
		#    'additionalQueryStringParams': {'test': "hello"}
		# }
	)

	app.register_blueprint(swagger)

def init_routes():
	for bp in blueprints:
		app.register_blueprint(bp)
	
	init_swagger()

def create_app():
	app_config = get_config()
	app.config.from_object(app_config)

	init_extensions()

	init_routes()

	@app.route("/users2")
	def t():
		return "teste"
	
	return app
