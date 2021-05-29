from game.code import Code 
from game.check import Check
from game.guess import Guess
from game.player import Player
from game.end_game import End_game

guess = Guess()
check = Check()
code = Code()
end_game = End_game()

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        keep_playing (boolean): Whether or not the game can continue.
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.code = ""
        self.PLayer1 = ""
        self.PLayer2 = ""
        self.turns = 0
   
    def start_game(self):
        """Called from the main function to start the game. Gets the 4 digit code from Code(). 
        Gets 2 players by calling the get player function. Gets the first guess from player 1. 
        Calls the function to turn the guess and the code into lists. Checks to see what numbers 
        if any are right.
        
        Args:
            self (Director): an instance of Director.
        
        """
        self.code = code.get_random_num()
        self.Player1 = self.get_player(1)
        self.Player2 = self.get_player(2)
        attempt = self.Player1.make_guess()
        guess.guess_lists(attempt, self.code)
        right_answer_list = guess.return_answer()
        num_guessed_list = guess.return_player_guess()
        check.check(num_guessed_list, right_answer_list)
        attempt = self.Player2.make_guess()
        guess.guess_lists(attempt, self.code)
        right_answer_list = guess.return_answer()
        num_guessed_list = guess.return_player_guess()
        output = check.check(num_guessed_list, right_answer_list)
        play = end_game.end_game(output)
        if play  == True:
            self.keep_playing()
        

    
    def get_player(self, num):
        """Gets the inputs at the beginning for each player on what the number is.

        Args:
            self (Director): An instance of Director.
            num (Guess): An instance of Guess.
        """

        name = input(f"What is the name for player number {num}? ")
        player = Player(name)
        return player

    def keep_playing(self):
        """Outputs that 2 players make a guess for the four digit number. if the number is right, they win, but if it is 
        wrong they keep playing

        Args:
            self (Director): An instance of Director.
        """

        if self.turns % 2 == 0:
            attempt = self.Player1.make_guess()
            guess.guess_lists(attempt, self.code)
            right_answer_list = guess.return_answer()
            num_guessed_list = guess.return_player_guess()
            output = check.check(num_guessed_list, right_answer_list)
            play = end_game.end_game(output)
            self.turns += 1
            if play == True:
                self.keep_playing()

        else:
            attempt = self.Player2.make_guess()
            guess.guess_lists(attempt, self.code)
            right_answer_list = guess.return_answer()
            num_guessed_list = guess.return_player_guess()
            output = check.check(num_guessed_list, right_answer_list)
            play = end_game.end_game(output)
            self.turns += 1
            if play  == True:
                self.keep_playing()
        
        


    

