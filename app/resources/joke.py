import json
from flask import jsonify, request
from flask_restful import Resource
from app.adapters.general_joke_adapter import JokeEspecificRequest
from app.models.joke import Joke as JokeModel
import random


class Joke(Resource):

    def get(self, origin=None):
        if not origin:
            keys_dict = list(JokeEspecificRequest.joke_origins.keys())
            origin = random.choice(keys_dict)
        return JokeEspecificRequest.get_joke(origin)

    def post(self, origin=None):
        json_data = request.get_json(force=True)
        joke_text = json_data["joke_text"]
        joke_obj = JokeModel(joke_text)
        return joke_obj.save()

    def put(self, origin=None):
        json_data = request.get_json(force=True)
        joke_id = json_data["id"]
        joke_text = json_data["joke_text"]
        joke_obj = JokeModel(joke_text, joke_id)
        return joke_obj.update()

    def delete(self, origin=None):
        json_data = request.get_json(force=True)
        joke_id = json_data["id"]
        joke_obj = JokeModel(_id=joke_id)
        return joke_obj.delete()
