from flask import jsonify, request
from flask_restful import Resource

class Numeric(Resource):

    def get(self):
        args = request.args.to_dict()
        numbers = args.get("numbers", False)
        number = args.get("number", False)
        if numbers:
            pass
        elif number:
            pass
        else:
            return jsonify({"msg": "parameters not sent correctly"})
