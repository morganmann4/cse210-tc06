class Guess:

    def __init__(self):

        """ Inputs the players guess and outputs the answer

        Args: 
            self (Screen): An instance of Screen.
        """

        self.player_guess = []
        
        self.answer = []

    def guess_lists(self, guess, code):

        """Gets input from the player

        Args: 
            self (Screen): An instance of Screen.
            guess (string): the input from the user
            code (string): the output from the user

        """
        
        self.answer.clear()
        self.player_guess.clear()

        for num in guess:
            self.player_guess.append(num)
        

        for num in code:
            
            self.answer.append(num)

    
    def return_answer(self):
        """ returns answer inputed by player

        Args: 
            self (Screen): An instance of Player.

        Returns:
            output
        """

        return self.answer

    def return_player_guess(self):
        """Returns players guess to the screen

        Args: 
            self (Screen): An instance of Screen.

        Returns:
            player's guess
        """

        return self.player_guess





