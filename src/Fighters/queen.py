from src.Fighters.fighter import *
class Queen(Fighter):
    def __init__(self, game):
        super().__init__(
            game,
            QUEEN["symbol"],
            QUEEN["color"],
            QUEEN["starting_coords"][0],
            QUEEN["starting_coords"][1],
            QUEEN["damage"],
            QUEEN["health"],
            QUEEN["move_speed"],
            QUEEN["attack_speed"],
        )
        self._range = QUEEN["range"]
        self._last_moved = 'd'

    def attack(self):
        if not super().attack():
            return
        buildings = set()