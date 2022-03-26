from src.Fighters.player import *


class King(Player):
    def __init__(self, game):
        super().__init__(game, KING)

    def attack_loop(self, obj_list, buildings: set):
        for obj in obj_list:
            x, y = self.closest_point(obj)
            if abs(x - self._x[0]) + abs(y - self._y[0]) <= self._range:
                buildings.add(obj)

    def attacked_buildings(self):
        buildings = set()
        for building_type in self._collision_buildings:
            for building in building_type:
                x, y = self.closest_point(building)
                if abs(x - self._x[0]) + abs(y - self._y[0]) <= self._range:
                    buildings.add(building)
        return buildings


def add_king(game):
    game.king = King(game)
