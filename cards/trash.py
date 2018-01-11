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
