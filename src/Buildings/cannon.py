from src.Buildings.building import Building
from src.config import CANNON


class Cannon(Building):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            CANNON["symbol"],
            startx,
            starty,
            CANNON["height"],
            CANNON["width"],
            CANNON["health"],
        )
        self.damage = CANNON["damage"]
