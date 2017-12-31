#!/usr/bin/python3
#
#   This game is a coin flip game
#

#
#   Imports
#
import random

game_version = .1

print('Coin flip - version {:.1f}'.format(game_version))

prob = random.random()

print('Random number: {:.2f}'.format(prob))

if prob <= .5:
    print('Heads wins!')
else:
    print('Tails wins!')
