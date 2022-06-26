from flask import jsonify, request
from flask_restful import Resource
from app.models.numeric import Numeric as NumericModel


class Numeric(Resource):

    def get(self):
        args = request.args.to_dict()
        numbers = args.get("numbers", False)
        number = args.get("number", False)
        if numbers:
            numbers = [int(i) for i in numbers.split(",")]
            result = NumericModel.calculate_mcm_from_list_numbers(numbers)
            return jsonify({"value": result})
        elif number:
            result = NumericModel.add_1(int(number))
            return jsonify({"value": result})
        else:
            return jsonify({"msg": "parameters not sent correctly"})
