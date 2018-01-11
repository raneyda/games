#!/usr/bin/python3
'''This game is a roll the dice game

    Version .2 added the games/dice module
'''

#
#   Imports
#
import sys
sys.path.append('N:\dev\games\\')

import games.dice

game_version = .2

print('Dice - version {:.1f}'.format(game_version))

die1, die2 = games.dice.roll_die(), games.dice.roll_die()

print('Die 1: {:1d}, Die 2: {:1d}'.format(die1,die2))
