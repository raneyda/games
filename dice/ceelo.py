#!/usr/bin/python3
#
#   This game is called Cee-Lo
#
'''
    Rules to Cee-Lo (no banker)

    Each player rolls 3 Dice

    Roll 4,5,6 Automatic Win
    Roll 1,2,3 Automatic Lose
    Roll a pair and the odd dice is the kicker
     - Kicker value of 1 automatic lose
     - Kicker value of 6 automatic win

    A player rolls until they set a point.  The set point is the kicker
    of 2,3,4,5.  If no doubles are rolled player re-rolls.

    Trips (3 matching dice) are not treated differntly than doubles.

'''

#
#   Imports
#
import uuid
import random
import sys
import platform

if platform.system() == 'Windows':
    sys.path.append('N:\dev\games\\')
else:
    print("Module games likely didn't load as your platform isn't recognized")
    pass

import games.coin
import games.core
import games.dice

if (len(sys.argv)) > 1:
    myargs = games.core.getopts(sys.argv)
    #
    #   Parse arguments
    #
    if '-b' in myargs:
        try:
            int(myargs['-b']) > 1
            games.dice.CeeLoPlayer.default_bet = int(myargs['-b'])
        except ValueError:
            games.dice.show_arguments('CeeLo')

    if '-p' in myargs:
        try:
            int(myargs['-p']) > 1
            if (1 > int(myargs['-p']) < 9):
                number_of_players = int(myargs['-p'])
            else:
                number_of_players = games.core.set_number_of_players()
                #number_of_players = 4
        except ValueError:
            games.dice.show_arguments('CeeLo')
    else:
        number_of_players = games.core.set_number_of_players()
        #number_of_players = 4
else:
    number_of_players = games.core.set_number_of_players()
    #number_of_players = 4

#
#   Set constants
#
game_version = .2

#
#   Define variables
#
players = []

#   Initialize Players
for i in range(number_of_players):
    players.append(games.dice.CeeLoPlayer())

game = games.dice.CeeLo(players)
game.place_bets()
game.status()
while len(game.active_players) >= 2:
    game.play_round()

for player in game.active_players:
    print("Player {:d} wins!".format(player.player_id))
