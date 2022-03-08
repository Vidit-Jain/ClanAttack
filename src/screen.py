from src.config import GAME, MESSAGES
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
                for _ in range(self.width)
            ]
            for _ in range(self.height)
        ]
        self.last_render = time.monotonic()
        erase_screen()

    def should_render(self):
        return time.monotonic() - self.last_render > 1 / GAME["fps"]

    def add_health_bar(self, game):
        health = "King health: "
        for i in range(0, len(health)):
            self.screen[MESSAGES["stats"][0]][MESSAGES["stats"][1] + i] = health[i]

        if game.king is None:
            return

        bar = "+" * int(game.king.health * 10 / game.king.max_health)
        bar.ljust(10, " ")
        for i in range(0, len(bar)):
            self.screen[MESSAGES["stats"][0] + 1][MESSAGES["stats"][1] + i] = bar[i]

    def add_spells_bar(self, game):
        active = "Rage: " + ("ACTIVE" if game.rageActive else "INACTIVE")
        for i in range(0, len(active)):
            self.screen[MESSAGES["stats"][0] + 2][MESSAGES["stats"][1] + i] = active[i]
        rage = "Rages left: " + str(game.rageSpell.uses)
        for i in range(0, len(rage)):
            self.screen[MESSAGES["stats"][0] + 3][MESSAGES["stats"][1] + i] = rage[i]
        heal = "Heals left: " + str(game.healSpell.uses)
        for i in range(0, len(rage)):
            self.screen[MESSAGES["stats"][0] + 4][MESSAGES["stats"][1] + i] = heal[i]

    def add_game_end(self, win):
        message = "Victory!" if win == 1 else "Game Over!"
        for i in range(0, len(message)):
            self.screen[MESSAGES["game_end"][1]][MESSAGES["game_end"][0] + i] = message[
                i
            ]

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
        if obj is None:
            return
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
                for _ in range(self.width)
            ]
            for _ in range(self.height)
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
        self.add_health_bar(game)
        self.add_spells_bar(game)

        # hello = "Hello"
        # for i in range(0, len(hello)):
        #     self.screen[5][120 + i] = hello[i]
        if game.townhall is not None:
            self.add(game.townhall)
        if game.king is not None:
            self.add(game.king)
