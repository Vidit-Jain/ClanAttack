from src.Fighters.player import *
from src.config import QUEEN
import time


class Queen(Player):
    def __init__(self, game):
        super().__init__(game, QUEEN, "Queen")
        self._tile_dimension = QUEEN["tile_dimension"]
        self.last_ultimate = time.monotonic()
        self._ultimate_range = QUEEN["ultimate_range"]
        self._ultimate_sound_file = QUEEN["ultimate_sound_file"]
        self._ultimate_attack_speed = QUEEN["ultimate_attack_speed"]
        self._ultimate_tile_dimension = QUEEN["ultimate_tile_dimension"]

    def ult_damage(self):
        buildings = self.check_tile_collision(
            self.ultimate_location, self._ultimate_tile_dimension
        )
        for obj in buildings:
            obj.damaged(self._damage * (self.game.rage.get_active() + 1))

    def check_tile_collision(self, starting, dimension):
        dummy = Object(
            self.game,
            " ",
            COLORS["RED"],
            starting[0],
            starting[1],
            dimension,
            dimension,
            1,
        )
        buildings = set()
        for building_type in self.game.enemy_buildings:
            for building in building_type:
                if dummy.collide(building):
                    buildings.add(building)
        return buildings

    def find_corner(self, attack_range, dimension):
        starting = [0, 0]
        if self._last_direction == "d":
            starting = [attack_range, 0]
        elif self._last_direction == "w":
            starting = [0, -attack_range]
        elif self._last_direction == "a":
            starting = [-attack_range, 0]
        elif self._last_direction == "s":
            starting = [0, attack_range]
        starting = [
            starting[0] + self._x[0] - dimension // 2,
            starting[1] + self._y[0] - dimension // 2,
        ]
        return starting

    def ultimate_attack(self):
        if (time.monotonic() - self.last_ult) <= 1 / self._ultimate_attack_speed:
            return
        starting = self.find_corner(self._ultimate_range, self._ultimate_tile_dimension)
        self.ultimate_location = starting.copy()
        self.last_ult = time.monotonic()
        self.game.y = 1
        self.ult_attack = True
        play(self._ultimate_sound_file)

    def attacked_buildings(self):
        starting = self.find_corner(self._range, self._tile_dimension)
        return self.check_tile_collision(starting, self._tile_dimension)


def add_queen(game):
    game.player = Queen(game)
