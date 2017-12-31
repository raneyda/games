#!/usr/bin/python3
#
#   This game is a roll the dice game
#

#
#   Imports
#
import random

#
#
#
def roll_dice():
    dice_value = 0
    prob = random.random()
    # print('Random number: {:.2f}'.format(prob))
    if prob <= .166:
        # print('1')
        dice_value = 1 
    elif prob > .166 and prob <= .332:
        # print('2')
        dice_value = 2 
    elif prob > .332 and prob <= .498:
        # print('3')
        dice_value = 3 
    elif prob > .498 and prob <= .664:
        # print('4')
        dice_value = 4 
    elif prob > .664 and prob <= .83:
        # print('5')
        dice_value = 5 
    else:
        # print('6')
        dice_value = 6 

    return dice_value

game_version = .1

print('Dice - version {:.1f}'.format(game_version))

die1, die2 = roll_dice(), roll_dice()

print('Die 1: {:1d}, Die 2: {:1d}'.format(die1,die2))
