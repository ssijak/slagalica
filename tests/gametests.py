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

    def test_moj_broj(self):
        from app.model.games.moj_broj_game import MojBroj
        game = MojBroj.create_game()
        self.assertIn(game.two_digit, [10, 15, 20])
        self.assertIn(game.tree_digit, [25, 50, 75, 100])
        self.assertGreater(game.result, 0)
        self.assertLess(game.result, 1000)
        print("{} {} {} - {}".format(game.one_digits, game.two_digit, game.tree_digit, game.result))
        result = game.guess("(15 + 3) * 5 - 4 / 2 + 100")  # 188
        import math
        self.assertEqual(result, math.fabs(game.result - 188))
        result = game.guess("((5*4)+4))*10 - ((1")
        self.assertEqual(result, "ERR_INVALID_SYNTAX")



if __name__ == '__main__':
    unittest.main()