import __future__
from operator import add, sub, mul, truediv
import itertools
import random

__author__ = 'ssijak@gmail.com'

ops = ['+', '-', '/', '*']
ops_map = {'+': add, '-': sub, '/': truediv, '*': mul}


def generate_numbers():
    numbers = [random.randint(1, 9) for _ in range(4)]  # small numbers
    numbers.append(random.choice([10, 15, 25]))  # middle numbers
    numbers.append(random.choice([50, 75, 100]))  # largest number
    target = random.randint(1, 999)  # requested solution
    return numbers, target


def check_solution(solution, goal):
    try:
        result = eval(compile(solution, '<string>', 'eval', __future__.division.compiler_flag))
        same = True if result == goal else False
        return same, result
    except (ValueError, SyntaxError):
        pass
    return False, None


def solve(numbers, target):
    best_value = target
    best_item = None

    def iter_combinations(seq):
        if len(seq) == 1:
            yield seq[0], str(seq[0])
        else:
            for i in range(len(seq)):
                left, right = seq[:i], seq[i:]  # split input list at i`th place
                # generate cartesian product
                for l, l_str in iter_combinations(left):
                    for r, r_str in iter_combinations(right):
                        for op in ops:
                            if ops_map[op] is truediv and r == 0:  # cant divide by zero
                                continue
                            else:
                                yield ops_map[op](float(l), r), \
                                    ('(' + l_str + op + r_str + ')')

    def remove_parentheses(expression):
        """Remove unneeded parentheses from math expression

        Args:
            expression - math expression

        Returns:
            Forwarded expression but without parentheses
            that are not needed and that do not affected
            the result of the math expression.
        """
        exp_result = eval(compile(expression, '<string>', 'eval', __future__.division.compiler_flag))
        current_exp = expression
        not_good = True
        while not_good:
            not_good = False
            for left, character in enumerate(current_exp):
                if character == '(':
                    right = left + 1
                    opened = 1
                    while right < len(current_exp) and opened > 0:
                        if current_exp[right] == '(':
                            opened += 1
                        elif current_exp[right] == ')':
                            opened -= 1
                        right += 1
                    if opened == 0:
                        check = current_exp[:left] + current_exp[left+1:]
                        check = check[:right-2] + check[right-1:]
                        if eval(compile(check, '<string>', 'eval', __future__.division.compiler_flag)) == exp_result:
                            current_exp = check
                            not_good = True
                            break
        return current_exp

    # Generates all permutations and combinations from given numbers and test
    for i in range(len(numbers)):
        for current in itertools.permutations(numbers, i+1):
            for value, item in iter_combinations(list(current)):
                if value < 0:
                    continue

                if abs(target - value) < best_value:
                    best_value = abs(target - value)
                    best_item = item

    return remove_parentheses(str(best_item)), best_value

#test = generate_numbers()
#print("Zadati brojevi su {}, a trazeni broj je {}".format(test[0], test[1]))
#print("Najbolje resenje je {}, a razdaljina od trazenog broja je {}".format(*solve(*test)))