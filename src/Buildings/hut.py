from src.Buildings.building import Building
from src.config import HUT


class Hut(Building):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            HUT["symbol"],
            startx,
            starty,
            HUT["height"],
            HUT["width"],
            HUT["health"],
        )
