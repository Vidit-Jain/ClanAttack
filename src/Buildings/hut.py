from src.Buildings.building import Building
from src.config import HUT, INITPOS


class Hut(Building):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            "hut",
            HUT["symbol"],
            startx,
            starty,
            HUT["height"],
            HUT["width"],
            HUT["health"],
        )


def add_huts(game):
    game.huts = []
    for i in range(0, len(INITPOS["huts"])):
        game.huts.append(Hut(game, INITPOS["huts"][i][0], INITPOS["huts"][i][1]))
