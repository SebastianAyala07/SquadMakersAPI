import os
import requests
from requests.structures import CaseInsensitiveDict

from app.common.joke_origin_target import TargetJoke

headers = CaseInsensitiveDict()


class DadAdapter(TargetJoke):

    @staticmethod
    def get_random_joke():
        headers["Accept"] = "application/json"
        base_url = str(os.getenv("DAD"))
        response = requests.get(base_url, headers=headers)
        response = response.json()
        json_to_return = {
            "id": response.get("id", 0),
            "joke": response.get("joke", "")
        }
        return json_to_return