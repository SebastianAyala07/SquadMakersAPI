import math
from functools import reduce

class Numeric:
    @staticmethod
    def calculate_mcm_from_list_numbers(numbers):
        def mcm(a, b):
            if a > b:
                greater_than = a
            else:
                greater_than = b

            while True:
                if greater_than % a == 0 and greater_than % b == 0:
                    mcm = greater_than
                    break
                greater_than += 1

            return mcm

        return reduce(lambda x, y: mcm(x, y), numbers)

    @staticmethod
    def add_1(number):
        return number + 1
