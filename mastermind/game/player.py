class Player:
    '''keeps track of the person playing the game, their identity and their last move'''


    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
            name (Player): an instance of Player
        """
        self.name = name

    def make_guess(self):
        """Guesses the 4 digit number inputted by the plater.

        Args:
            self (Player): an instance of Player.
            guess (Move): an instance of Move
        """

        guess = input(f"Make a 4 digit guess, {self.name}. ")
        return str(guess)

