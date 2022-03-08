from src.game_input import *
from src.screen import *
from src.Fighters.king import *
from src.Buildings.townhall import *
from src.config import *


class Game:
    def __init__(self):
        self.input = Get()
        self.screen = Screen()
        self.king = King(self, 0, 0)
        self.screen.add(self.king)
        self.townhall = Townhall(self)
        self.screen.add(self.townhall)

    def handle_input(self):
        ch = input_to(self.input)
        if ch in KING["control_keys"]:
            self.king.move(ch)
        if ch == "c":
            return 1
        return 0

    def loop(self):
        while 1:
            self.screen.render()
            if self.handle_input() == 1:
                break


game = Game()
game.screen.erase_screen()
game.loop()
