from src.building import *
from src.config import *


class Townhall(Building):
    def __init__(self, game, startx, starty):
        super().__init__(
            game,
            TOWNHALL["symbol"],
            startx,
            starty,
            TOWNHALL["height"],
            TOWNHALL["width"],
            TOWNHALL["health"],
        )
