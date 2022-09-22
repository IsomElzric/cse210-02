"""

"""


from random import randint


class Card():
    def __init__(self):
        self.value = 0

    def draw(self):
        self.value = randint(1, 13)