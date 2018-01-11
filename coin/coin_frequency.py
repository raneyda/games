#!/usr/bin/python3
"""Flip a coin some number of times and print the frequency of heads and tails

"""
#
#   Imports
#
import collections
import sys
sys.path.append('N:\dev\games\\')

import games.coin

game_version = .1

def main_function():
    print('Coin flip frequency - version {:.1f}'.format(game_version))

    how_many = 10000
    my_collection = collections.Counter()
    for i in range(how_many):
        the_roll = games.coin.flipcoin()
        my_collection.update(the_roll[:1])

    my_collection = collections.OrderedDict(sorted(my_collection.items()))

    for k, v in my_collection.items():
        print("{}, {:d}, {:.2f}".format(k, v, (v / how_many)*100 ))


if __name__ == '__main__':
    main_function()
