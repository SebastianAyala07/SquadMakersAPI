from flask import jsonify, request
from flask_restful import Resource

class Numeric(Resource):

    def get(self):
        json_data = request.get_json(force=True)
        numbers = json_data.get("numbers", False)
        number = json_data.get("number", False)
        if numbers:
            pass
        elif number:
            pass
        else:
            return jsonify({"msg": "parameters not sent correctly"})
