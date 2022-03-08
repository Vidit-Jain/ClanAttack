from src.Buildings.building import *
from src.config import *


class Spawnpoint(Building):
    def __init__(self, game, startx, starty):
        super().__init__(
            game,
            SPAWNPOINT["symbol"],
            startx,
            starty,
            SPAWNPOINT["height"],
            SPAWNPOINT["width"],
            SPAWNPOINT["health"],
        )
