from src.config import GAME
from src.object import Object
import time
import sys


def set_cursor(x=0, y=0):
    print("\033[" + str(x) + ";" + str(y) + "H")


def erase_screen():
    print("\033[2J")


class Screen:
    def __init__(self):
        self.height = GAME["window"]["height"]
        self.width = GAME["window"]["width"]
        self.screen = [
            [
                GAME["background"] + GAME["color"] + GAME["symbol"]
                for i in range(self.width)
            ]
            for i in range(self.height)
        ]
        self.last_render = time.monotonic()
        erase_screen()

    def should_render(self):
        return time.monotonic() - self.last_render > 1 / GAME["fps"]

    def render(self):
        if not self.should_render():
            return
        set_cursor()
        output = ""
        for i in self.screen:
            for j in i:
                output += j
            output += "\n"
        sys.stdout.write(output)
        self.last_render = time.monotonic()

    def add(self, obj: Object):
        symbol = obj.color + GAME["background"] + obj.symbol
        for i in range(int(obj.y[0]), int(obj.y[1])):
            for j in range(int(obj.x[0]), int(obj.x[1])):
                self.screen[i][j] = symbol

    def remove(self, obj: Object):
        for i in range(int(obj.y[0]), int(obj.y[1])):
            for j in range(int(obj.x[0]), int(obj.x[1])):
                self.screen[i][j] = GAME["background"] + GAME["color"] + GAME["symbol"]

    def clear(self):
        self.screen = [
            [
                GAME["background"] + GAME["color"] + GAME["symbol"]
                for i in range(self.width)
            ]
            for i in range(self.height)
        ]

    def loop_add(self, obj: list[Object]):
        if obj is not None:
            for i in range(0, len(obj)):
                self.add(obj[i])

    def add_to_screen(self, game):
        self.loop_add(game.spawnpoints)
        self.loop_add(game.huts)
        self.loop_add(game.cannons)
        self.loop_add(game.walls)
        self.loop_add(game.barbarians)

        if game.townhall is not None:
            self.add(game.townhall)
        if game.king is not None:
            self.add(game.king)
