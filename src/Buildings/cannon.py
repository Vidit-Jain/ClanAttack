import time
from subprocess import DEVNULL, STDOUT, check_call, Popen
from src.Buildings.building import Building
from src.config import CANNON, INITPOS
from src.audio import *


class Cannon(Building):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            "cannon",
            CANNON["symbol"],
            startx,
            starty,
            CANNON["height"],
            CANNON["width"],
            CANNON["health"],
        )
        self.damage = CANNON["damage"]
        self.attack_speed = CANNON["attack_speed"]
        self.last_attacked = 0
        self.range = CANNON["range"]

    def attack(self, obj):
        if obj is None:
            return
        if time.monotonic() - self.last_attacked < 1 / self.attack_speed:
            return
        self.last_attacked = time.monotonic()
        play("src/AudioFiles/cannon.mp3")
        obj.damaged(self.damage)

    def __dist(self, obj):
        if obj is None:
            return 1e6
        return abs(self.x[0] - obj.x[0]) + abs(self.y[0] - obj.y[0])

    def shoot(self):
        best = None
        for barbarian in self.game.barbarians:
            if self.__dist(barbarian) < self.__dist(best):
                best = barbarian
        if self.game.king is not None and self.__dist(self.game.king) < self.__dist(
            best
        ):
            best = self.game.king

        if self.__dist(best) > self.range:
            return
        self.attack(best)


def add_cannons(game):
    game.cannons = []
    for i in range(0, len(INITPOS["cannons"])):
        game.cannons.append(
            Cannon(game, INITPOS["cannons"][i][0], INITPOS["cannons"][i][1])
        )
