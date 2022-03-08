from src.object import Object
from src.config import BUILDING


class Building(Object):
    def __init__(self, game, symbol: str, startx: int, starty: int, height: int, width: int, health: int):
        super().__init__(
            game, symbol, BUILDING["colors"][-1], startx, starty, height, width, health
        )
