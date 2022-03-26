from src.Fighters.fighter import *
from src.audio import *


class King(Fighter):
    def __init__(self, game):
        super().__init__(
            game,
            KING["symbol"],
            KING["color"],
            KING["starting_coords"][0],
            KING["starting_coords"][1],
            KING["damage"],
            KING["health"],
            KING["move_speed"],
            KING["attack_speed"],
            KING["sound_file"]
        )
        self._range = KING["range"]

    def attack_loop(self, obj_list, buildings: set):
        for obj in obj_list:
            x, y = self.closest_point(obj)
            if abs(x - self._x[0]) + abs(y - self._y[0]) <= self._range:
                buildings.add(obj)

    def attack(self):
        if not super().attack():
            return
        buildings = set()
        for building_type in self._collision_buildings:
            self.attack_loop(building_type, buildings)
        for obj in buildings:
            obj.damaged(self._damage * (self.game.rage.get_active() + 1))

    def move(self, ch: str):
        if ch == "w":
            super().move(0, -1)
        elif ch == "a":
            super().move(-1, 0)
        elif ch == "s":
            super().move(0, 1)
        elif ch == "d":
            super().move(1, 0)
        else:
            self.attack()


def add_king(game):
    game.king = King(game)
