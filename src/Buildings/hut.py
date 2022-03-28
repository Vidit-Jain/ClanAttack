from src.Buildings.building import Building
from src.config import HUT, INITPOS


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


def add_huts(game, level):
    game.huts = []
    for i in range(0, len(INITPOS["huts"][level])):
        game.huts.append(
            Hut(game, INITPOS["huts"][level][i][0], INITPOS["huts"][level][i][1])
        )
