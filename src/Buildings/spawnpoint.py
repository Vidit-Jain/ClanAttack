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
    if game.barbarian_count <= 0:
        return
    spawnpoint = game.spawnpoints[ord(ch[0]) - ord("1"[0])]
    game.barbarian_count -= 1
    game.barbarians.append(Barbarian(game, spawnpoint.get_x()[0], spawnpoint.get_y()[0]))


def add_spawnpoints(game):
    game.spawnpoints = []
    for i in range(0, len(INITPOS["spawnpoints"])):
        game.spawnpoints.append(
            Spawnpoint(game, INITPOS["spawnpoints"][i][0], INITPOS["spawnpoints"][i][1])
        )
