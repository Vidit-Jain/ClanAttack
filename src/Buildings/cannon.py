import time
from subprocess import DEVNULL, STDOUT, check_call, Popen
from src.Buildings.building import Building
from src.config import CANNON, INITPOS
from src.audio import *


class Cannon(Building):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            CANNON["symbol"],
            startx,
            starty,
            CANNON["height"],
            CANNON["width"],
            CANNON["health"],
        )
        self._damage = CANNON["damage"]
        self._attack_speed = CANNON["attack_speed"]
        self._last_attacked = 0
        self._range = CANNON["range"]

    def attack(self, obj):
        if obj is None:
            return
        if time.monotonic() - self._last_attacked < 1 / self._attack_speed:
            return
        self._last_attacked = time.monotonic()
        play("src/AudioFiles/cannon.mp3")
        obj.damaged(self._damage)

    def __dist(self, obj):
        if obj is None:
            return 1e6
        return abs(self._x[0] - obj.get_x()[0]) + abs(self._y[0] - obj.get_y()[0])

    def shoot(self):
        best = None
        for i in range(len(self.game.troops) - 1):
            for troop in self.game.troops[i]:
                if self.__dist(troop) < self.__dist(best):
                    best = troop
        if self.game.player is not None and self.__dist(self.game.player) < self.__dist(
            best
        ):
            best = self.game.player

        if self.__dist(best) > self._range:
            return
        self.attack(best)


def add_cannons(game):
    game.cannons = []
    for i in range(0, len(INITPOS["cannons"])):
        game.cannons.append(
            Cannon(game, INITPOS["cannons"][i][0], INITPOS["cannons"][i][1])
        )
