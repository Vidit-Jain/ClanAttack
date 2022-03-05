from src.game_input import *
from src.screen import *
from src.config import *
from src.object import *
from src.king import *
from colorama import Fore


class Game:
    def __init__(self):
        self.input = Get()
        self.screen = Screen()
        self.obj = Object(self, "+", Fore.RED, 10, 3, 5, 5, 100)
        self.king = King(self, 0, 0)
        self.screen.add(self.obj)
        self.screen.add(self.king)

    def loop(self):
        while 1:
            self.screen.render()
            a = input_to(self.input)
            if a == "s":
                self.king.movedown()


game = Game()
game.screen.erase_screen()
game.loop()
