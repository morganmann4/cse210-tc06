import random

class Code:
    """collects random numbers from 1000 to 9999"""

    def __init__(self):
     """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.

        Returns:
            integer: The user's input as an integer.
        """
     self.random_num = random.randint(1000, 9999)

    def get_random_num(self):
     """Gets numerical input from the user through the screen.
          
        Args: 
            self (Screen): An instance of Screen.
       Returns:
            integer: The user's input as an random integer.
        """
    #print(self.random_num)
    return str(self.random_num)
