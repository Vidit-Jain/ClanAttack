from src.Fighters.troop import Troop
from src.config import BALLOON
from src.audio import *
import random


class Balloon(Troop):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            BALLOON["symbol"],
            BALLOON["colors"][-1],
            startx,
            starty,
            BALLOON["damage"],
            BALLOON["health"],
            BALLOON["move_speed"],
            BALLOON["attack_speed"],
            BALLOON["colors"],
            [game.huts, game.cannons, game.townhall]
        )

    def damaged(self, damage: int):
        self.__update_color()
        super().damaged(damage)

    def attack(self, obj):
        if not super(Troop, self).attack():
            return
        play("src/AudioFiles/barbarian_attack.mp3")
        obj.damaged(self._damage * (self.game.rage.get_active() + 1))
