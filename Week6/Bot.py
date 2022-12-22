import random

class Bot:
    def __init__(self, name = 'Bot player - X'):
        self.name = name
        self.label = 'X'
    
    def move(self, left_position):
        move =  random.randrange(1, left_position+1)
        print(f"{self.name}, choosed {move} \n")
        return move