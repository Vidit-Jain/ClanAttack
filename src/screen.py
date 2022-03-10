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
        self._height = GAME["window"]["height"]
        self._width = GAME["window"]["width"]
        self._screen = [
            [
                GAME["background"] + GAME["color"] + GAME["symbol"]
                for _ in range(self._width)
            ]
            for _ in range(self._height)
        ]
        self._last_render = time.monotonic()
        erase_screen()

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def should_render(self):
        return time.monotonic() - self._last_render > 1 / GAME["fps"]

    def add_health_bar(self, game):
        health = "King health: "
        for i in range(0, len(health)):
            self._screen[MESSAGES["stats"][0]][MESSAGES["stats"][1] + i] = health[i]

        if game.king is None:
            return

        bar = "+" * int(game.king.get_health() * 10 / game.king.get_max_health())
        bar.ljust(10, " ")
        for i in range(0, len(bar)):
            self._screen[MESSAGES["stats"][0] + 1][MESSAGES["stats"][1] + i] = bar[i]

    def add_spells_bar(self, game):
        active = "Rage: " + ("ACTIVE" if game.rage.get_active() else "INACTIVE")
        for i in range(0, len(active)):
            self._screen[MESSAGES["stats"][0] + 2][MESSAGES["stats"][1] + i] = active[i]
        rage = "Rages left: " + str(game.rage.get_uses_left())
        for i in range(0, len(rage)):
            self._screen[MESSAGES["stats"][0] + 3][MESSAGES["stats"][1] + i] = rage[i]
        heal = "Heals left: " + str(game.healSpell.get_uses_left())
        for i in range(0, len(rage)):
            self._screen[MESSAGES["stats"][0] + 4][MESSAGES["stats"][1] + i] = heal[i]

    def add_game_end(self, win):
        message = "Victory!" if win == 1 else "Game Over!"
        for i in range(0, len(message)):
            self._screen[MESSAGES["game_end"][1]][MESSAGES["game_end"][0] + i] = message[
                i
            ]

    def render(self, game):
        if not self.should_render():
            return
        set_cursor()

        game.frames.append(self._screen)
        output = ""
        for i in self._screen:
            for j in i:
                output += j
            output += "\n"
        sys.stdout.write(output)
        self._last_render = time.monotonic()

    def add(self, obj: Object):
        if obj is None:
            return
        symbol = obj.get_color() + GAME["background"] + obj.get_symbol()
        for i in range(int(obj.get_y()[0]), int(obj.get_y()[1])):
            for j in range(int(obj.get_x()[0]), int(obj.get_x()[1])):
                self._screen[i][j] = symbol

    def remove(self, obj: Object):
        for i in range(int(obj.get_y()[0]), int(obj.get_y()[1])):
            for j in range(int(obj.get_x()[0]), int(obj.get_x()[1])):
                self._screen[i][j] = GAME["background"] + GAME["color"] + GAME["symbol"]

    def clear(self):
        self._screen = [
            [
                GAME["background"] + GAME["color"] + GAME["symbol"]
                for _ in range(self._width)
            ]
            for _ in range(self._height)
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

        if game.townhall is not None:
            self.add(game.townhall)
        if game.king is not None:
            self.add(game.king)
