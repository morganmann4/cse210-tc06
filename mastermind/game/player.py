class Player:
    '''keeps track of the person playing the game, their identity and their last move'''


    def __init__(self, name):
        self.name = name

    def make_guess(self):

        guess = input(f"Make a 4 digit guess, {self.name}. ")
        return str(guess)

