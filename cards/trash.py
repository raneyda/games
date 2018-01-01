#!/usr/bin/python3


'''

    This game is called trash

    This is a two player card game.  The deck is shuffled and each player is
    dealt 10 cards face down (in two rows of 5).  The remainder of the deck is
    face down between the two players.

    The first player (youngest) takes a card from the deck.  If the card is any
    card from an Ace to a 10 it is put in the corresponding position with the
    Ace on the top left and the 10 in the bottom right.  The player then looks
    at the replaced card and places it in the corresponding spot.

    Kings are wild and can be playing in any spot.

    The players turn ends when a card is picked up that has no place to go or
    when a jack or queen in drawn.  At that point the player discards the card
    in their hand in the 'trash'.

    The next player can 'dig in the trash' (choose from the discarded card) or
    draw.  Play continues until one player has repalced all face-down cards with
    face-up cards.

    The second round is played with only 9 cards.  The game ends when a player
    gets down to one card and wins that round.

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
