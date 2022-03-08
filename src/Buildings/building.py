from src.object import *
from src.config import *


class Building(Object):
    def __init__(self, game, symbol, startx, starty, height, width, health):
        super().__init__(
            game, symbol, BUILDING["colors"][-1], startx, starty, height, width, health
        )
