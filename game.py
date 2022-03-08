from src.game_input import *
from src.screen import *
from src.Fighters.king import *
from src.Buildings.townhall import *
from src.Buildings.spawnpoint import *
from src.Buildings.hut import *
from src.Buildings.cannon import *
from src.Buildings.wall import *
from src.config import *


class Game:
    def __init__(self):
        self.input = Get()
        self.screen = Screen()

        self.king = King(self)

        self.townhall = Townhall(self)

        self.spawnpoints = []
        for i in range(0, len(INITPOS["spawnpoints"])):
            self.spawnpoints.append(Spawnpoint(self, INITPOS["spawnpoints"][i][0], INITPOS["spawnpoints"][i][1]))
        self.huts = []
        for i in range(0, len(INITPOS["huts"])):
            self.huts.append(Hut(self, INITPOS["huts"][i][0], INITPOS["huts"][i][1]))
        self.cannons = []
        for i in range(0, len(INITPOS["cannons"])):
            self.cannons.append(Cannon(self, INITPOS["cannons"][i][0], INITPOS["cannons"][i][1]))
        self.walls = []
        self.walls.extend(create_wall(self, [5, 10], [10, 10]))

    def handle_input(self):
        ch = input_to(self.input)
        if ch in KING["control_keys"]:
            self.king.move(ch)
        if ch == "c":
            return 1
        return 0

    def loop(self):
        while 1:
            self.screen.clear()
            self.screen.add_to_screen(self)
            self.screen.render()
            if self.handle_input() == 1:
                break


game = Game()
erase_screen()
game.loop()
