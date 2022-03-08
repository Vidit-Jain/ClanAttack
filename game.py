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
        self.king = None
        self.townhall = None
        self.input = Get()
        self.screen = Screen()
        self.x = 0

        add_king(self)
        add_townhall(self)

        add_spawnpoints(self)
        add_huts(self)
        add_walls(self)
        add_cannons(self)
        self.barbarians = []

    def handle_input(self):
        ch = input_to(self.input)
        if ch in KING["control_keys"]:
            self.king.move(ch)
        elif ch in SPAWNPOINT["control_keys"]:
            self.barbarians.append(spawn(game, ch))
        if ch == "c":
            print(self.x)
            return 1
        return 0

    def remove_destroyed(self):
        for barbarian in self.barbarians:
            if barbarian.destroyed:
                self.barbarians.remove(barbarian)

        for wall in self.walls:
            if wall.destroyed:
                self.walls.remove(wall)

        for hut in self.huts:
            if hut.destroyed:
                self.x = 1
                self.huts.remove(hut)

        for cannon in self.cannons:
            if cannon.destroyed:
                self.cannons.remove(cannon)

        if self.king is not None and self.king.destroyed:
            self.king = None

        if self.townhall is not None and self.townhall.destroyed:
            self.townhall = None

    def move_barbarians(self):
        for barbarian in self.barbarians:
            barbarian.move()

    def loop(self):
        while 1:
            self.screen.clear()
            self.screen.add_to_screen(self)
            self.move_barbarians()
            self.remove_destroyed()
            self.screen.render()
            if self.handle_input() == 1:
                break


game = Game()
erase_screen()
game.loop()
