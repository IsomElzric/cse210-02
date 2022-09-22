"""

"""


from game.card import Card


class Game():
    def __init__(self):
        self.card = Card()
        self.score = 300
    
    def start_game(self):
        self.card.draw()
        self.do_output()

    def get_input(self):
        return input("Higher or lower? [h/l] ")

    def do_update(self, old_card):
        pass

    def do_output(self):
        print("The card is: {}".format(self.card.value))

        guess = self.get_input()
        
        old_card = self.card.value
        self.card.draw()

        print("Next card was: {}".format(self.card.value))

        self.do_update()

    def check_win(self):
        pass