"""
card.py
Holds our card class for the game of hilo.

for CSE 210 w02
by Alexander Turner
"""


from random import randint


class Card():
    """
    The Card class holds our information about the value
    of the card, as well as the function to draw a new one.
    """
    def __init__(self):
        """
        Initializes the value to 0.
        """
        self.value = 0

    def draw(self):
        """
        Draws a new card, replacing the value of our card object.
        """
        self.value = randint(1, 13)