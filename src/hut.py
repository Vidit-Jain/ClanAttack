from src.building import *
from src.config import *


class Hut:
    def __init__(self, game, startx, starty):
        super().__init__(
            self,
            game,
            HUT["symbol"],
            HUT["color"],
            startx,
            starty,
            HUT["height"],
            HUT["width"],
            HUT["health"],
        )
