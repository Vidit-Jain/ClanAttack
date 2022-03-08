from src.Buildings.building import Building
from src.config import SPAWNPOINT


class Spawnpoint(Building):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            SPAWNPOINT["symbol"],
            startx,
            starty,
            SPAWNPOINT["height"],
            SPAWNPOINT["width"],
            SPAWNPOINT["health"],
        )
