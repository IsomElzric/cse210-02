"""

"""


from game.card import Card


class Game():
    def __init__(self):
        self.card = Card()
        self.score = 300
        self.run = True
    
    def start_game(self):
        self.card.draw()
        self.do_output()

    def get_input(self):
        return input("Higher or lower? [h/l] ")

    def do_update(self):
        old_card = self.card.value
        guess = self.get_input()
        self.card.draw()
        
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
        while self.run:
            print()
            print("The card is: {}".format(self.card.value))
            self.do_update()
            print("Next card was: {}".format(self.card.value))
            print("Your score is: {}".format(self.score))
            
            if input("Play again? [y/n] ") == "n":
                self.run = False