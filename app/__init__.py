from flask import Flask
from flask_restful import Api
from app.resources.joke import RandomJoke, Joke
from db.mysql import mysql

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)
    mysql.init_app(app)

    api = Api(app, catch_all_404s=True)
    api.add_resource(RandomJoke, "/random-joke/", "/random-joke/<string:origin>")
    api.add_resource(Joke, "/joke/", "/joke/<string:origin>")

    app.url_map.strict_slashes = False

    @app.route("/")
    def home():
        return "Hello World"

    return app
