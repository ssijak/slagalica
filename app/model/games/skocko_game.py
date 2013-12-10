__author__ = 'Perun'


class SkockoGame():

    MAX_GUESS = 6

    def __init__(self):
        self.solved = False
        self.fields = None

    @classmethod
    def create_game(cls):
        game = cls()
        import random
        game.fields = [random.randrange(6),
                       random.randrange(6),
                       random.randrange(6),
                       random.randrange(6)]
        return game

    def guess(self, combination):
        if len(combination) != 4:
            return "ERR_INVALID_COMBINATION"
        elements = self.fields[:]
        correct = 0
        has_number = 0
        j = 0
        size = len(combination)
        i = 0
        while i < size:
            if combination[i] == elements[j]:
                correct += 1
                del elements[j]
                del combination[i]
                size -= 1
                continue
            j += 1
            i += 1
        i = 0
        while i < size:
            j = 0
            while j < len(elements):
                if combination[i] == elements[j]:
                    has_number += 1
                    del elements[j]
                    break
                j += 1
            i += 1

        result = dict()
        result['correct'] = correct
        result['has_number'] = has_number
        if correct == 4:
            self.solved = True
        return result
