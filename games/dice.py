'''Module for dice functions of games
'''
#
#   Imports
#
import random

#
#   Begin dice functions
#
def roll_die():
    '''Function to roll a die and return a value 1 - 6
    '''
    return rpg_die(6)

def rpg_die(sides, percentile=0):
    '''Function to roll a die and return a value based on the numbers of sides

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
    '''
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

def shoot_dice(combo, percentile=0):
    '''Allows for multiple device to be rolled and returned
    '''

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
