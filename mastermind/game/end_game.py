
class End_game:
    '''checks to see if the game is over'''
    

    def end_game(self, output):

        for letter in output:
            if letter != 'x':
                return True
        print("Game over, you win!!!")
        return False
       

