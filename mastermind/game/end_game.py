
class End_game:
    """checks to see if the game is over"""
    

    def end_game(self, output):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            output (Screen): An instance of Screen.

        Returns:
             Game over, you win !!! if x is outputted
        """

        for letter in output:
            if letter != 'x':
                return True
        print("Game over, you win!!!")
        return False
       

