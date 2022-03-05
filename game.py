from src.game_input import *
from src.screen import * 
from src.config import *
from src.object import *
from colorama import Fore
class Game:
    def __init__(self):
        self.input = Get()
        self.screen = Screen()
        self.obj = Object(self, "+", Fore.RED, 10, 3, 5, 5)
        self.screen.add(self.obj)
    def loop(self):
        while (1):
            self.screen.render();
    
game = Game()
game.loop()