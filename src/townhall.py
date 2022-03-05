from src.building import *
from src.config import *


class Townhall:
    def __init__(self, game, startx, starty):
        super().__init__(
            self,
            game,
            TOWNHALL["symbol"],
            TOWNHALL["color"],
            startx,
            starty,
            TOWNHALL["height"],
            TOWNHALL["width"],
            TOWNHALL["health"],
        )
