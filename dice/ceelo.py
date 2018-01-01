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
import random

#
#   Set constants
#
game_version = .1

#
#   Define variables
#
num_players = 4
push_round = 0
betting_pool = 0
current_round = 0
player_points = []
player_banks = []
player_bet = []
active_players = []


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
def shoot_dice(player_number):
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
#   Print the players banks
#
def print_banks(number_of_players):
    #   Print current banks
    total_bank = 0
    for i in range(number_of_players):
        print('Current bank of player {:1d}: {:1d}'.format(i+1, player_banks[i]))
        total_bank += player_banks[i]
    #print('Betting pool: {:1d}.  Total of banks: {:1d}'.format(betting_pool,total_bank))
    return

#
#   Place a $10 bet for each remaining player (bank > 0)
#
def place_bets(players):
    #   Place bets
    minimum_bet = 20
    for player in players:
        if player_banks[player] > 0:
            player_bet[player] = minimum_bet
            player_banks[player] = player_banks[player] - minimum_bet
            player_points[player] = 0
    return

#
#   A testing routine to determine what point each player had
#
def print_setpoints(players):
    for player in players:
        if (player_points[player] != 0):
            print('Player {:1d} setpoint is: {:1d}'.format(player+1, player_points[player]))
    return

#
#   Plays a single round of Cee-Lo and determines the winner or pushes to
#   the next round with only those players that push
#
def play_round(players):
    #
    # Define local constants
    #
    setpoint = 0
    setpoint_player = 0
    global betting_pool
    point = 0
    push = 0

    #
    #   Reset points to zero for all players
    #
    for i in range(num_players):
        player_points[i] = 0

    for player in players:
        point = 0
        while point == 0:
            point = shoot_dice(player+1)
        if (point != 1) and (point != 6) and (player_points[player] == 0) and (setpoint == 0):
            player_points[player] = point
            setpoint = player_points[player]
            setpoint_player = player
            print('Player {:1d} sets point at ({:1d})'.format(player+1,point))
        elif (point == 1):
            player_points[player] = point
            betting_pool = betting_pool + player_bet[player]
            player_bet[player] = 0
            print('Player {:1d} automatic loss!'.format(player+1))
        elif (point == 6):
            player_points[player] = point
            for l in players:
                if player_bet[l] > 0:
                    betting_pool = betting_pool + player_bet[l]
                    player_bet[l] = 0
            player_banks[player] = player_banks[player] + betting_pool
            betting_pool = 0
            print('Player {:1d} automatic win!'.format(player+1))
            push = 0
            break
        else:
            player_points[player] = point
            if setpoint > player_points[player]:
                betting_pool = betting_pool + player_bet[player]
                player_bet[player] = 0
                print('Player {:1d} loses! ({:1d})'.format(player+1,point))
            elif setpoint < player_points[player]:
                betting_pool = betting_pool + player_bet[setpoint_player]
                player_bet[setpoint_player] = 0
                setpoint = point
                setpoint_player = player
                print('Player {:1d} has highest hand! ({:1d})'.format(player+1,point))
                push = 0
            else:
                print('Player {:1d} pushes! ({:1d})'.format(player+1,point))
                push = 1

    #
    #   Payout the winner or tally the bets
    #
    if (push == 0) and (point != 6):
        for l in range(num_players):
            if player_bet[l] > 0:
                betting_pool = betting_pool + player_bet[l]
                player_bet[l] = 0

        player_banks[setpoint_player] += betting_pool
        betting_pool = 0
        print('Player {:1d} wins! ({:1d})'.format(setpoint_player+1,player_points[setpoint_player]))
    else:
        for l in range(num_players):
            if player_bet[l] > 0:
                betting_pool = betting_pool + player_bet[l]
                player_bet[l] = 0

    return push

#
#   Determines the number of remainin players as a list
#   remaining players are those with a bank > 0
#   Shuffles the list so the first player is always different
#
def find_active_players(fa_push=0):
    # Reset current active players

    # Determine if previous round was a push
    if fa_push == 1:
        #print('Finding active pushed players')
        push_players = max(player_points)

        for i in range(num_players):
            if player_points[i] == push_players:
                #print('Push player {:1d} bank: {:1d}, point: {:1d}'.format(i+1,player_banks[i],player_points[i]))
                active_players.insert(i, i)

    # If not a push then add all players with a current bank
    else:
        #print('Finding regular active players')

        for i in range(num_players):
            if player_banks[i] > 0:
                active_players.insert(i, i)
                #print('Player {:1d}, round index: {:1d}'.format(i+1,i + players_remaining % (current_round+1)))


    random.shuffle(active_players)
    #print(active_players)
    return

def find_winner():
    for i in range(num_players):
        if player_banks[i] != 0:
            print('Game over! Player {:1d} wins!'.format(i+1))
    return

def count_players(push_count):
    number_of_players = 0
    for i in range(num_players):
        if player_banks[i] > 0:
            number_of_players += 1
    if (push_count == 1) and (number_of_players == 1):
        return 2
    else:
        return number_of_players
#
#   Begin main program
#
print('Cee-lo - version {:.1f}'.format(game_version))

#
#   Take number of players as input
#
#try:
#    int(input("Number of players (default - 2): "), num_players)
#except ValueError:
#    num_players = 2

if (num_players > 6) or (num_players < 0):
    print('Invalid number of players.  Setting players to 2')
    num_players = 2
else:
    print('Number of players is: {:1d}'.format(num_players))

players_remaining = num_players

#
#   Setup initial players
#
for i in range(num_players):
    player_points.insert(i, 0)
    player_banks.insert(i, 100)
    player_bet.insert(i, 0)

find_active_players()

#
#   Print initial banks
#
print_banks(num_players)

#
#   Start game with all players
#
while players_remaining > 1:
    #   Show round number and remaining number of players
    print('=========\nRound {:1d}\nPlayers remainaing: {:1d}\n---------'.format(current_round+1,players_remaining))

    if betting_pool == 0:
        place_bets(active_players)
    push_round = play_round(active_players)

    current_round += 1
    #print_setpoints(active_players)
    print_banks(num_players)
    active_players = []

    # Find active players
    find_active_players(push_round)
    players_remaining = count_players(push_round)
    input('Press Enter to continue to next round')

find_winner()
