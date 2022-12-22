# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import random
from Human import Human
from Bot import Bot
from Game import Game

if __name__ == '__main__':
    with_bot = input('Playing with bot?  (Y/N)').upper()

    game = None
    if(with_bot == 'Y'):
        game =  Game(Human(), Bot()) #Default player settings, Human  - O, Bot - X. 
    else :
        game = Game(Human(), Human("X"))
    
    winner = None
    while winner == None:
        player = game.swith_player()
        print(game.board)
        game.make_move(player)
        winner = game.get_winner()

    print(f"Winner is: {winner.name}\n--------- \n{game.board}")
   
