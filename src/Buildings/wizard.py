import time
from subprocess import DEVNULL, STDOUT, check_call, Popen
from src.Buildings.building import Building
from src.object import Object
from src.config import WIZARD, INITPOS, COLORS
from src.audio import *


class Wizard(Building):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            WIZARD["symbol"],
            startx,
            starty,
            WIZARD["height"],
            WIZARD["width"],
            WIZARD["health"],
        )
        self._damage = WIZARD["damage"]
        self._attack_speed = WIZARD["attack_speed"]
        self._last_attacked = 0
        self._range = WIZARD["range"]
        self._tile_dimension = WIZARD["tile_dimension"]

    def attack(self, obj):
        if obj is None:
            return
        if time.monotonic() - self._last_attacked < 1 / self._attack_speed:
            return
        self._last_attacked = time.monotonic()
        play("src/AudioFiles/wizard_attack.mp3")
        dummy = Object(
            self.game,
            " ",
            COLORS["RED"],
            obj.get_x()[0] - self._tile_dimension // 2,
            obj.get_y()[0] - self._tile_dimension // 2,
            self._tile_dimension,
            self._tile_dimension,
            999,
        )
        obj_list = []
        for troop_type in self.game.troops:
            for troop in troop_type:
                if troop.collide(dummy):
                    obj_list.append(troop)

        if not self.game.player.is_destroyed() and dummy.collide(self.game.player):
            obj_list.append(self.game.player)

        for damaged_troop in obj_list:
            damaged_troop.damaged(self._damage)

    def __dist(self, obj):
        if obj is None:
            return 1e6
        return abs(self._x[0] - obj.get_x()[0]) + abs(self._y[0] - obj.get_y()[0])

    def shoot(self):
        best = None
        for troop_arr in self.game.troops:
            for troop in troop_arr:
                if self.__dist(troop) < self.__dist(best):
                    best = troop
        if (not self.game.player.is_destroyed()) and self.__dist(
            self.game.player
        ) < self.__dist(best):
            best = self.game.player

        if self.__dist(best) > self._range:
            return
        self.attack(best)


def add_wizards(game):
    game.wizards = []
    for i in range(0, len(INITPOS["wizards"])):
        game.cannons.append(
            Wizard(game, INITPOS["wizards"][i][0], INITPOS["wizards"][i][1])
        )
