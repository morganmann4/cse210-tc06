class Check:
    """Gets text or numerical input and displays text ouput"""


    def check(self, player_guess, answer):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            player_guess (string): The prompt to display to the user.
            answer (string): The input from the user.

        Returns:
            Output x, o, *
        """
        output = []
        for i in range(0, len(answer)):

            if player_guess[i] == answer[i]:
                output.append("x")

            elif player_guess[i] == answer[0] or player_guess[i] == answer[1] or player_guess[i] == answer[2] or player_guess[i] == answer[3]:
                output.append("o")
            else:
                output.append("*")
        print(output)
        return output
        








