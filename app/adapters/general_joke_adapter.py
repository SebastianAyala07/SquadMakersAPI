from app.adapters.dad_adapter import DadAdapter
from app.adapters.chuck_adapter import ChuckAdapter
from flask import jsonify

class JokeEspecificRequest:

    joke_origins = {
        "chuck": ChuckAdapter,
        "dad": DadAdapter
    }

    @classmethod
    def get_joke(cls, origin):
        try:
            adapter = cls.joke_origins[str.lower(origin)]
            response = adapter.get_random_joke()
        except Exception as e:
            response = jsonify(
                {
                    "msg": "The origin of which the joke is wanted does not exist"
                }
            )
        return response
