from src.building import *
from src.config import *


class Hut(Building):
    def __init__(self, game, startx, starty):
        super().__init__(
            self,
            game,
            HUT["symbol"],
            startx,
            starty,
            HUT["height"],
            HUT["width"],
            HUT["health"],
        )
