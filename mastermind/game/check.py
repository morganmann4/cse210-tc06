class Check:
    '''Gets text or numerical input and displays text ouput'''


    def check(self, player_guess, answer):
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
        








