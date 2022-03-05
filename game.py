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

    def handle_input(self):
        ch = input_to(self.input)
        if ch == "s":
            self.king.movedown()
        if ch == "w":
            self.king.moveup()
        if ch == "a":
            self.king.moveleft()
        if ch == "d":
            self.king.moveright()
        if ch == "c":
            return 1 
        return 0

    def loop(self):
        while 1:
            self.screen.render()
            if (self.handle_input() == 1):
                break


game = Game()
game.screen.erase_screen()
game.loop()
