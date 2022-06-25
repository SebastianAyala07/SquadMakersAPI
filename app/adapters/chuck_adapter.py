import os
import requests
from app.common.joke_origin_target import TargetJoke

class ChuckAdapter(TargetJoke):

    @staticmethod
    def get_random_joke():
        base_url = str(os.getenv("CHUCK")) + "/jokes/random"
        response = requests.get(base_url)
        response = response.json()
        json_to_return = {
            "id": response.get("id", 0),
            "joke": response.get("value", "")
        }
        return json_to_return
