from src.Buildings.building import *
from src.config import *


class Wall(Building):
    def __init__(self, game, startx, starty):
        super().__init__(
            game,
            WALL["symbol"],
            startx,
            starty,
            WALL["height"],
            WALL["width"],
            WALL["health"],
        )
