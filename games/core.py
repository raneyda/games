'''Module for dice functions of games
'''
#
#   Imports
#
import random
from collections import deque

#
#   Define Classes
#
def set_number_of_players():
    '''Allows input of number of playerss, return a valid number of players
    '''
    print("Getting number of players")
    try:
        num_players = int(input("Number of players (default - 2): "))
    except ValueError:
        print('Invalid number of players.  Setting players to 2')
        num_players = 2

    if (num_players > 8) or (num_players < 0):
        print('Invalid number of players.  Setting players to 2')
        num_players = 2
    else:
        print('Number of players is: {:1d}'.format(num_players))

    return num_players


def player_order(passed_players, setpoint=0):
    ''' Determines a random order of players based list of players
        Returns an list of player instances
    '''
    total_players = 0
    player_list = []
    for player in passed_players:
        # Determine if a player is inactive (zero bank)
        if (setpoint == 0) and (player.bank == 0):
            player.active = False

        if (setpoint != 0) and (player.point == setpoint) and (player.active):
            # List of pushed players
            player_list.append(player)
        elif player.active:
            # List of active players
            player_list.append(player)
    total_players = len(player_list)

    random_start = int(random.uniform(0, total_players))
    rotated_list = deque(player_list)
    rotated_list.rotate(random_start)
    return rotated_list
