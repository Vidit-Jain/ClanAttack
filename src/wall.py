from src.building import *
from src.config import *


class Wall:
    def __init__(self, game, startx, starty):
        super().__init__(
            self,
            game,
            WALL["symbol"],
            WALL["color"],
            startx,
            starty,
            WALL["height"],
            WALL["width"],
            WALL["health"],
        )
