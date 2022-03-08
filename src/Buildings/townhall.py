from src.Buildings.building import *
from src.config import *


class Townhall(Building):
    def __init__(self, game):
        super().__init__(
            game,
            TOWNHALL["symbol"],
            TOWNHALL["starting_coords"][0],
            TOWNHALL["starting_coords"][1],
            TOWNHALL["height"],
            TOWNHALL["width"],
            TOWNHALL["health"],
        )