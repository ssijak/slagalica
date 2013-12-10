__author__ = 'Perun'
import unittest
import random


class SkockoGameUnitTest(unittest.TestCase):

    def test_skocko(self):
        from app.model.games.skocko_game import SkockoGame
        game = SkockoGame.create_game()
        print("fields: {}".format(game.fields))
        self.assertEqual(len(game.fields), 4)
        for i in range(SkockoGame.MAX_GUESS):
            combination = [random.randrange(6),
                           random.randrange(6),
                           random.randrange(6),
                           random.randrange(6)]
            print("Combination {}".format(combination))
            result = game.guess(combination)
            print("Result [{}]: {}".format(i, result))
            if game.solved:
                print("Solved in {}".format(i))
                break


if __name__ == '__main__':
    unittest.main()