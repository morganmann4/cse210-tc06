class Guess:

    def __init__(self):

        self.player_guess = []
        
        self.answer = []

    def guess_lists(self, guess, code):
        
        self.answer.clear()
        self.player_guess.clear()

        for num in guess:
            self.player_guess.append(num)
        

        for num in code:
            
            self.answer.append(num)

    
    def return_answer(self):

        return self.answer

    def return_player_guess(self):

        return self.player_guess





