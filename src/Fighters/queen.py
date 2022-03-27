from src.Fighters.player import *
from src.config import QUEEN


class Queen(Player):
    def __init__(self, game):
        super().__init__(game, QUEEN, "Queen")
        self._tile_dimension = QUEEN["tile_dimension"]

    def attacked_buildings(self):
        buildings = set()
        starting = [0, 0]
        if self._last_direction == "d":
            starting = [self._range, 0]
        elif self._last_direction == "w":
            starting = [0, -self._range]
        elif self._last_direction == "a":
            starting = [-self._range, 0]
        elif self._last_direction == "s":
            starting = [0, self._range]

        starting = [
            starting[0] + self._x[0] - self._tile_dimension // 2,
            starting[1] + self._y[0] - self._tile_dimension // 2,
        ]
        dummy = Object(
            self.game,
            " ",
            COLORS["RED"],
            starting[0],
            starting[1],
            self._tile_dimension,
            self._tile_dimension,
            1,
        )
        for building_type in self.game.enemy_buildings:
            for building in building_type:
                if dummy.collide(building):
                    buildings.add(building)

        return buildings


def add_queen(game):
    game.player = Queen(game)
