from src.fighter import *


class Barbarian(Fighter):
    def __init__(self, game, startx, starty):
        super().__init__(
            game,
            BARBARIAN["color"],
            BARBARIAN["symbol"],
            startx,
            starty,
            BARBARIAN["damage"],
            BARBARIAN["health"],
            BARBARIAN["move_speed"],
        )
