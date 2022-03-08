from src.Buildings.building import *
from src.config import *


class Townhall(Building):
    def __init__(self, game):
        super().__init__(
            game,
            TOWNHALL["symbol"],
            TOWNHALL["startx"],
            TOWNHALL["starty"],
            TOWNHALL["height"],
            TOWNHALL["width"],
            TOWNHALL["health"],
        )
