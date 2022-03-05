from src.building import *
from src.config import *


class Spawnpoint:
    def __init__(self, game, startx, starty):
        super().__init__(
            self,
            game,
            SPAWNPOINT["symbol"],
            SPAWNPOINT["color"],
            startx,
            starty,
            SPAWNPOINT["height"],
            SPAWNPOINT["width"],
            SPAWNPOINT["health"],
        )
