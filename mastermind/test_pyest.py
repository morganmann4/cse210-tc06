import pytest as py
from game.end_game import End_game
from game.player import Player
from game.director import Director
from game.code import Code
from game.guess import Guess
from game.check import Check



def test_end_game():
    end_game = End_game()
    output = ['*', '*', '*', '*']
    assert end_game.end_game(output) == True


def test_guess_lists():
        guesses = Guess()
        guess = str(1123)
        code = str(1234)
        guesses.guess_lists(guess, code)
        assert guesses.player_guess == ['1', '1', '2', '3']
        assert guesses.answer == ['1', '2', '3', '4']

def test_check():
    check = Check()
    guess = ["2", "4", "6", "8"]
    answer = ["2", "3", "8", "9"]
    check.check(guess, answer)
    assert output == ["x", "*", "o", "*"]


py.main(["-v", "--tb=no", "test_pytest.py"]) 