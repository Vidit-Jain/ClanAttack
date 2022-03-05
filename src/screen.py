from src.config import *
from colorama import Fore
import time
import sys


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

    def set_cursor(self, x=0, y=0):
        print("\033[" + str(x) + ";" + str(y) + "H")

    def erase_screen(self):
        print("\033[2J")

    def should_render(self):
        return time.monotonic() - self.last_render > 1 / GAME["fps"]

    def render(self):
        # self.erase_screen()
        if not self.should_render():
            return
        self.set_cursor()
        output = ""
        for i in self.screen:
            for j in i:
                output += j
            output += "\n"
        sys.stdout.write(output)
        self.last_render = time.monotonic()

    def add(self, obj):
        symbol = obj.color + GAME["background"] + obj.symbol
        for i in range(int(obj.y[0]), int(obj.y[1])):
            for j in range(int(obj.x[0]), int(obj.x[1])):
                self.screen[i][j] = symbol

    def remove(self, obj):
        for i in range(int(obj.y[0]), int(obj.y[1])):
            for j in range(int(obj.x[0]), int(obj.x[1])):
                self.screen[i][j] = GAME["background"] + GAME["color"] + GAME["symbol"]
