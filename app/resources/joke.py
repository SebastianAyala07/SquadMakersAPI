from flask_restful import Resource
from app.adapters.general_joke_adapter import JokeEspecificRequest
import random



class RandomJoke(Resource):
    def get(self, origin=None):
        if not origin:
            keys_dict = list(JokeEspecificRequest.joke_origins.keys())
            origin = random.choice(keys_dict)
        return JokeEspecificRequest.get_joke(origin)
