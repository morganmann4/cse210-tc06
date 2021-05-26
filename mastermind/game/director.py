from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster


class director:
    
    def __init__(self):
        self.keep_playing = True

   
    def start_game(self):
        '''starts the game and keeps the game running until there is a winner'''
        
        self.prepare_game(self)
        
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_ouputs()


    
    
    def prepare_game(self):
        '''Prepares the game before it begins by getting players name and adding it to the roster'''
        for r in range(2):
            name = input("")

    def get_inputs(self):
        '''gets the moves from current player at the beginning of each round'''

    def do_updates(self):
        '''updates game information each round such as board with current move'''

    def do_outputs(self):
        '''Outputs important game info after each round. Checks if number was guessed correctly'''

    

