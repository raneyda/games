"""Module for dice functions of games
"""
#
#   Imports
#
import random

import sys
import platform

if platform.system() == 'Windows':
    sys.path.append('N:\dev\games\\')
else:
    print("Module games likely didn't load as your platform isn't recognized")


import games.core

#
#   Define Classes
#
class DicePlayer:
    """A player of a dice game
    """
    starting_bank = 100
    default_bet = 10
    player_id = 1
    def __init__(self):
        self.player_id = DicePlayer.player_id
        self.bank = self.starting_bank
        self.bet = 0
        self.point = 0
        self.dice = []
        self.active = True
        self.lost = None
        DicePlayer.player_id += 1
        return

class CeeLoPlayer(DicePlayer):
    """A player of a CeeLo dice game
    """
    def __repr__(self):
        return("Player {:d}, bank: {:d}, current bet: {:d}, last roll: {:d}".format(self.player_id,self.bank,self.bet,self.point))

    def ante(self):
        """Player bets
        """
        if (self.bank > 0) and (self.active):
            self.bet = self.default_bet
            self.bank -= self.bet
            self.bet == 0
        return

    def roll_the_dice(self, combo):
        """Player rolls dice
        """
        self.dice = shoot_dice(combo)
        self.point = ceelo_dice(self.dice)
        if self.point == 1:
            self.lost = True
        print('Player {:1d}, Die 1: {:1d}, Die 2: {:1d}, Die 3: {:1d}, Point: {:d}'.format(self.player_id, self.dice[0], self.dice[1], self.dice[2], self.point))
        return

class CeeLo:
    """The CeeLo game includes a list of players
    """
    def __init__(self, instance_players):
        self.push = False
        self.setpoint = 0
        self.players = instance_players
        self.payout = 0
        self.auto_winner = False
        self.active_players = games.core.player_order(self.players)
        self.round = 1
        return

    def play_round(self):
        """Play one round of Cee Lo
        """
        # Define tuples
        singles = (1,2,3,4,5,6)
        trips = (111,222,333,444,555,666)

        for player in self.active_players:
            while (player.point == 0) and (self.auto_winner is False):
                player.roll_the_dice("3D6")
                if player.point == -1:
                    # Player loses - empty bank
                    player.lost = True
                    print("LOSE - Automatic on roll [1, 2, 3]".format(self.setpoint, player.point))
                elif player.point == 9:
                    # Player wins - pay out bank
                    self.payout_bank(player)
                    self.setpoint = player.point
                    self.auto_winner = True
                    print("WINNER - Automatic on roll [4, 5, 6]".format(self.setpoint, player.point))
                    break
                elif ([x for x in singles if x == player.point]) or ([x for x in trips if x == player.point]):
                    # Undetermined state - set player point
                    if player.point > self.setpoint:
                        self.setpoint = player.point
                        print("New  - Setpoint: {:d}, Player point: {:d}".format(self.setpoint, player.point))
                    elif player.point == self.setpoint:
                        self.push = True
                        print("PUSH - Setpoint: {:d}, Player point: {:d}".format(self.setpoint, player.point))
                    else:
                        player.lost = True
                        print("LOSE - Setpoint: {:d}, Player point: {:d}".format(self.setpoint, player.point))

        # Need to evaluate players that didn't lose.
        for player in self.active_players:
            if (player.active) and (player.point == self.setpoint) and (self.push is False):
                self.payout_bank(player)

        # Reset active players
        self.active_players = []
        self.round += 1

        # Did we push this round?
        if self.push:
            # Only keep players that pushed
            print("Round pushed - bank is: {:d}".format(self.payout))
            self.active_players = games.core.player_order(self.players, self.setpoint)
            self.status()
            self.reset_round()
            self.push = False
        else:
            # Round reset
            self.active_players = games.core.player_order(self.players)
            if len(self.active_players) > 1:
                self.place_bets()
            self.status()
            self.reset_round()
        return

    def reset_round(self):
        for player in self.players:
            player.point = 0
            player.lost = None
            player.dice = []
            player.trips = False
        self.setpoint = 0
        self.auto_winner = False
        return

    def payout_bank(self, player):
        player.bank += self.payout
        self.payout = 0
        return

    def place_bets(self):
        for player in self.players:
            if (player.bank > 0) and (player.active):
                player.ante()
                self.payout += player.bet
                print("Player {:d} bets {:d} - payout is {:d}".format(player.player_id, player.bet, self.payout))
        return

    def status(self):
        if len(self.active_players) > 1:
            if self.push:
                print("===============\nRound {:d} - PUSH\n---------------\nPayout: {:d}\n---------------".format(self.round,self.payout))
            else:
                print("===============\nRound {:d}\n---------------\nPayout: {:d}\n---------------".format(self.round,self.payout))
            for player in self.players:
                if player.active:
                    print(player)
            print("===============")
        else:
            print("===============\nRound {:d}\n---------------\nPayout: {:d}\n---------------".format(self.round,self.payout))
        return
#
#   Begin dice functions
#
def roll_die():
    """Function to roll a die and return a value 1 - 6
    """
    return rpg_die(6)

def rpg_die(sides, percentile=0):
    """Function to roll a die and return a value based on the numbers of sides

    Roleplaying games (rpg) use 7 dice sets

    Die styles are:
        D4 (tetrahedron), returns 1-4
        D6 (The cube), returns 1-6
        D8 (Octahedron), returns 1-8
        D10 (Pentagonal Trapezohedron), returns 0-9
        D10 [Percentile], returns 00-90 incrementing by 10
        D12 (Dodecahedron), returns 1-12
        D20 (Icosahedron), returns 1-20

    Based on the numebr of sides return a value for that type of die
    """
    if type(sides) is not int:
        return 0

    prob = random.random()

    if sides == 6 or sides == 4 or sides == 8 or sides == 12 or sides == 20:
        return int((prob) / (1 / sides))+1
    elif percentile == 1:
        prob = int(random.random() * 10) * 10
        if prob == 0:
            prob = str('00')
        return prob
    elif sides == 10:
        prob = int(random.random() * 10)
        return prob
    else:
        return 0

def shoot_dice(combo="1D6", percentile=0):
    """Allows for multiple device to be rolled and returned

    The format is xDy, where x is the number of dice and y is sides of the die
    Examples:
    1D6 would roll (1) 6 sided die
    3D6 would roll (3) 6 sided dice
    2D4 would roll (2) 4 sided dice

    if no argument is given it defaults to "1D6"
    """

    if type(combo) is not str:
        return 0

    dice, sides = combo.split("D")
    rolls = []

    if percentile == 1 and sides == 10:
        rolls.append(rpg_die(int(sides),percentile))
    else:
        for i in range(int(dice)):
            rolls.append(rpg_die(int(sides),percentile))
    return rolls

def ceelo_dice(rolled_dice):
    """Take in a list of dice, sort them and evaluate whether a valid combo

        Takes in a list of (3) numbers
        Returns:
           -1 = automatic loss
            9 = automatic win
          xxx = trips
            x = valid combination, point
    """
    rolled_dice.sort()

    if (rolled_dice[0] == rolled_dice[1] and rolled_dice[2]) or (rolled_dice[1] == rolled_dice[2]):
        # We have a point to set
        if (rolled_dice[0] == rolled_dice[1] == rolled_dice[2]):
            return int(str(rolled_dice[0])+str(rolled_dice[1])+str(rolled_dice[2]))
        elif rolled_dice[0] == rolled_dice[1]:
            return rolled_dice[2]
        else:
            return rolled_dice[0]
    elif (rolled_dice[0] == 1 and rolled_dice[1] == 2 and rolled_dice[2] == 3):
        # print('Automatic lose!!')
        return -1
    elif (rolled_dice[0] == 4 and rolled_dice[1] == 5 and rolled_dice[2] == 6):
        # print('Automatic win!!')
        return 9
    # no point set, not a combination
    return 0

def show_arguments(game):
    if game == 'CeeLo':
        print("==================\nUsage: ceelo.py -p <num> -b <bum>\n\n   -p   number of players from 2 - 8\n   -b   default bet from 1 to 100\n")
        sys.exit()
    return
