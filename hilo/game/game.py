"""
game.py
Holds our game class for the game of hilo.

for CSE 210 w02
by Alexander Turner
"""


from game.card import Card


class Game():
    """
    The game class holds our functions to loop through and run the game.
    """
    def __init__(self):
        """
        Initializes our card object, sets the score, and sets the game loop running.
        """
        self.card = Card()
        self.score = 300
        self.run = True
    
    def start_game(self):
        """
        Draws our first card and begins the game loop.
        """
        self.card.draw()
        self.do_output()

    def get_input(self):
        """
        Gets the user's guess and returns it.
        """
        return input("Higher or lower? [h/l] ")

    def do_update(self):
        """
        Compares the old value with the new card value and determines if
        the players guess was correct, then adjusts the score, and checks
        if the game has been lost.
        """
        old_card = self.card.value
        guess = self.get_input()
        self.card.draw()
        
        # Make sure that we never draw duplicates
        while self.card.value == old_card:
            self.card.draw()

        if guess == "h":
            if self.card.value > old_card:
                self.score += 100
            
            else:
                self.score -= 75
        
        elif guess == "l":
            if self.card.value < old_card:
                self.score += 100
            
            else:
                self.score -= 75

        if self.score <= 0:
            self.run = False

    def do_output(self):
        """
        Runs our loop and displays our game to the player.
        """
        while self.run:
            print()
            print("The card is: {}".format(self.card.value))
            self.do_update()
            print("Next card was: {}".format(self.card.value))
            print("Your score is: {}".format(self.score))
            
            if input("Play again? [y/n] ") == "n":
                self.run = False