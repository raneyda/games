#!/usr/bin/python3


'''

    This game is called street craps

    All players roll dice to determine who goes first (random order in This
    version)

    Place bets on if the shooters passes (rolls a 7 or 11) or
    craps out (2, 3 or 12).  The shooter bets first and the other players must
    match his bet.

    The shooter rolls two dice
        - If the shoort neither passes or craps out the number rolled becomes
          the point
        - The shooter continues rolling until the point or 7 is reached

    Ways to win (or lose) after the first roll:
        - Bets that the shooter would pass become bets the shooter will re-roll
          the point before rolling a 7.
        - Bets other than pass win if the shooter gets a 7
'''

#
#   Imports
#
import random

#
#   Set constants
#
game_version = .1

#
#   Define variables
#


#
#   Functions
#

#
#   Roll a 6 sided die one time
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

#
#   Roll 3 dice, sort, and return the value as 1-6
#
def shoot_dice():
    dice = [roll_dice(), roll_dice(), roll_dice()]
    dice.sort()

    print('Player {:1d}, Die 1: {:1d}, Die 2: {:1d}, Die 3: {:1d}'.format(player_number, dice[0],dice[1],dice[2]))

    if (dice[0] == dice[1] and dice[2] != (1 or 6)) or (dice[1] == dice[2] and dice[0] != (1 or 6)):
        # Set the point
        if dice[0] == dice[1]:
            return dice[2]
        else:
            return dice[0]
    if (dice[0] == 1 and dice[1] == 2 and dice[2] == 3):
        # print('Automatic lose!!')
        return 1
    if (dice[0] == 4 and dice[1] == 5 and dice[2] == 6):
        # print('Automatic win!!')
        return 6
    # no setpoint yet
    return 0

#
#   Begin main program
#
print('Street Craps - version {:.1f}'.format(game_version))
