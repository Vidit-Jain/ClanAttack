from src.Buildings.building import Building
from src.config import SPAWNPOINT, INITPOS
from src.Fighters.barbarian import *


class Spawnpoint(Building):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            "spawnpoint",
            SPAWNPOINT["symbol"],
            startx,
            starty,
            SPAWNPOINT["height"],
            SPAWNPOINT["width"],
            SPAWNPOINT["health"],
        )


def spawn(game, ch: str):
    spawnpoint = game.spawnpoints[ord(ch[0]) - ord("1"[0])]
    return Barbarian(game, spawnpoint.x[0], spawnpoint.y[0])


def add_spawnpoints(game):
    game.spawnpoints = []
    for i in range(0, len(INITPOS["spawnpoints"])):
        game.spawnpoints.append(
            Spawnpoint(game, INITPOS["spawnpoints"][i][0], INITPOS["spawnpoints"][i][1])
        )
