from src.fighter import *


class King(Fighter):
    def __init__(self, game, startx, starty):
        super().__init__(
            game,
            KING["color"],
            KING["symbol"],
            startx,
            starty,
            KING["damage"],
            KING["health"],
            KING["move_speed"],
        )
