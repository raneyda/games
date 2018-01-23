"""Module for coin functions of games
"""
#
#   Imports
#
import random

def flipcoin():
    """Function to return Heads or Tails of a coin flip
    """
    prob = random.random()

    if prob <= .49999:
        return "Heads"
    else:
        return "Tails"
