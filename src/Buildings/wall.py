from src.Buildings.building import *
from src.config import *


class Wall(Building):
    def __init__(self, game, startx, starty):
        super().__init__(
            game,
            WALL["symbol"],
            startx,
            starty,
            WALL["height"],
            WALL["width"],
            WALL["health"],
        )


def create_wall(game, start_wall, end_wall):
    walls = []
    for i in range(start_wall[0], end_wall[0] + 1):
        for j in range(start_wall[1], end_wall[1] + 1):
            walls.append(Wall(game, i, j))

    return walls
