from src.Buildings.building import Building
from src.config import SPAWNPOINT, INITPOS
from src.Fighters.barbarian import *
from src.Fighters.archer import *
from src.Fighters.balloon import *


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


def spawn(game, ch: str):
    a = ord(ch[0]) - ord("1"[0])
    b = a // 3
    if game.troop_count[b] <= 0:
        return
    spawnpoint = game.spawnpoints[a % 3]
    game.troop_count[b] -= 1
    if b == 0:
        game.barbarians.append(
            Barbarian(game, spawnpoint.get_x()[0], spawnpoint.get_y()[0])
        )
    elif b == 1:
        game.archers.append(Archer(game, spawnpoint.get_x()[0], spawnpoint.get_y()[0]))
    elif b == 2:
        game.balloons.append(
            Balloon(game, spawnpoint.get_x()[0], spawnpoint.get_y()[0])
        )


def add_spawnpoints(game, level):
    game.spawnpoints = []
    for i in range(0, len(INITPOS["spawnpoints"][level])):
        game.spawnpoints.append(
            Spawnpoint(
                game,
                INITPOS["spawnpoints"][level][i][0],
                INITPOS["spawnpoints"][level][i][1],
            )
        )
