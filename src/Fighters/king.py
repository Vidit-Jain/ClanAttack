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

    def movedown(self):
        self.move(0, 1)

    def moveup(self):
        self.move(0, -1)

    def moveleft(self):
        self.move(-1, 0)

    def moveright(self):
        self.move(1, 0)
