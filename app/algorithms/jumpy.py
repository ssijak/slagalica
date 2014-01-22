import random

__author__ = 'ssijak'

all_signs = ['s', 't', 'p', 'k', 'h']
PLACE_NUM = 4


def generate_combination():
    return [random.choice(all_signs) for _ in range(4)]


def check_combination(combo, given):
    num_good = 0
    num_bad_place = 0
    for i in range(PLACE_NUM):
        if combo[i] == given[i]:
            num_good += 1
            given[i] = 'X' #mark as used
        else:
            for j in range(PLACE_NUM):
                if combo[i] == given[j] and combo[j] != given[j]:
                    num_bad_place += 1
                    given[j] = 'X'
    return num_good, num_bad_place

