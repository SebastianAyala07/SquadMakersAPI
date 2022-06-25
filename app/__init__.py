from flask import Flask, url_for

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    @app.route("/")
    def home():
        return "Hello World"

    return app
