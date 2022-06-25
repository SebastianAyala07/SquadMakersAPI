from flask_restful import Resource
from app.adapters.general_joke_adapter import JokeEspecificRequest


class RandomJoke(Resource):
    def get(self, origin):
        return JokeEspecificRequest.get_joke(origin)

