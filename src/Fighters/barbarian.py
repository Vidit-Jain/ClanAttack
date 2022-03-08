from src.Fighters.fighter import *


class Barbarian(Fighter):
    def __init__(self, game, startx, starty):
        super().__init__(
            game,
            BARBARIAN["symbol"],
            BARBARIAN["color"],
            startx,
            starty,
            BARBARIAN["damage"],
            BARBARIAN["health"],
            BARBARIAN["move_speed"],
        )
