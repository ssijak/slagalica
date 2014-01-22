#!/usr/bin/python
 # -*- coding: utf-8 -*-
import codecs
import random
from collections import Counter
from sys import path

__author__ = 'ssijak'

all_letters = ['a', 'b', 'c', u'č', u'ć', 'd', u'dž', u'đ', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'lj', 'm', 'n', 'nj',
               'o', 'p', 'r', 's', u'š', 't', 'u', 'v', 'z', u'ž']
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', u'č', u'ć', 'd', u'dž', 'đ', 'f', 'g', 'h', 'j', 'k', 'l', 'lj', 'm', 'n', 'nj',
              'p', 'r', 's', u'š', 't', 'v', 'z', u'ž']


def generate_letters():
    return [random.choice(vowels * 6 + consonants) for _ in range(12)]


def check_word(word, letters):
    #word and letters are both sent as lists
    words = Counter(word)
    letters = Counter(letters)
    letters.subtract(words)
    for i in letters.items():
        if i[1] < 0:
            return False
    return True


def get_best_word(chosen):
    occurrences = {}
    for x in chosen:
        occurrences[x] = (occurrences[x] + 1) if x in occurrences else 1
    with codecs.open(path.join(path.dirname(__file__), 'sr.dic'), 'r', 'utf-16') as f: #this will not be from a file
        content = f.readlines()

    for item in reversed(content):
        item = item.lower().replace("\n", "")

        current = {}
        for x in item:
            current[x] = (current[x] + 1) if x in current else 1

        good = True
        for it in current.keys():
            if it not in occurrences or occurrences[it] < current[it]:
                good = False
                break
        if good:
            return item