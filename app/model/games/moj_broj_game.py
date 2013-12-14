__author__ = 'Perun'


class MojBroj:

    def __init__(self, one_digits, two_digit, tree_digit, result):
        self.one_digits = one_digits
        self.two_digit = two_digit
        self.tree_digit = tree_digit
        self.result = result

    @classmethod
    def create_game(cls):
        import random
        one_digits = [random.randrange(8)+1, random.randrange(8)+1, random.randrange(8)+1, random.randrange(8)+1]
        two_digit = (2+random.randrange(3)) * 5
        tree_digit = (1+random.randrange(4)) * 25
        result = 1 + random.randrange(999)
        game = cls(one_digits, two_digit, tree_digit, result)
        return game

    def guess(self, guess):
        try:
            result = eval(guess)
        except SyntaxError:
            return "ERR_INVALID_SYNTAX"
        import math
        print("Guess: {}. needed: {}, difference: {}".format(result, self.result, math.fabs(result - self.result)))
        return math.fabs(result - self.result)
