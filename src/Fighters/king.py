from src.Fighters.fighter import *


class King(Fighter):
    def __init__(self, game, startx, starty):
        super().__init__(
            game,
            KING["symbol"],
            KING["color"],
            startx,
            starty,
            KING["damage"],
            KING["health"],
            KING["move_speed"],
        )
    def move(self, ch):
        if ch == "s":
            super().move(0, 1)
        elif ch == "w":
            super().move(0, -1)
        elif ch == "a":
            super().move(-1, 0)
        else:
            super().move(1, 0)
