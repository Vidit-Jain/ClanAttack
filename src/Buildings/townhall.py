from src.Buildings.building import Building
from src.config import TOWNHALL


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


def add_townhall(game):
    game.townhall = Townhall(game)
