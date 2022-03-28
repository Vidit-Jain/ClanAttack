from src.Buildings.building import Building
from src.config import TOWNHALL


class Townhall(Building):
    def __init__(self, game, startx, starty):
        super().__init__(
            game,
            TOWNHALL["symbol"],
            startx,
            starty,
            TOWNHALL["height"],
            TOWNHALL["width"],
            TOWNHALL["health"],
        )


def add_townhall(game, level):
    game.townhall = [
        Townhall(
            game,
            TOWNHALL["starting_coords"][level][0],
            TOWNHALL["starting_coords"][level][1],
        )
    ]
