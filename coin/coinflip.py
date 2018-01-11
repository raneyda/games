#!/usr/bin/python3
'''This game is a coin flip game

    Version .2 extracts the functions into a module
'''

#
#   Imports
#
import sys
sys.path.append('N:\dev\games\\')

import games.coin

game_version = .2

print('Coin flip - version {:.1f}'.format(game_version))

print(games.coin.flipcoin(), "wins!")
