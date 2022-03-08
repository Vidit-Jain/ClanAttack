from src.Buildings.building import Building
from src.config import CANNON, INITPOS


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


def add_cannons(game):
    game.cannons = []
    for i in range(0, len(INITPOS["cannons"])):
        game.cannons.append(
            Cannon(game, INITPOS["cannons"][i][0], INITPOS["cannons"][i][1])
        )
