from src.building import *
from src.config import *


class Cannon(Building):
    def __init__(self, game, startx, starty, damage):
        super().__init__(
            self,
            game,
            CANNON["symbol"],
            startx,
            starty,
            CANNON["height"],
            CANNON["width"],
            CANNON["health"],
        )
        self.damage = damage
