from src.Buildings.building import Building
from src.config import WALL


class Wall(Building):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            "wall",
            WALL["symbol"],
            startx,
            starty,
            WALL["height"],
            WALL["width"],
            WALL["health"],
        )


def generate_wall(game, start_wall: list[int], end_wall: list[int]):
    walls = []
    for i in range(start_wall[0], end_wall[0] + 1):
        for j in range(start_wall[1], end_wall[1] + 1):
            walls.append(Wall(game, i, j))

    return walls


def add_walls(game):
    game.walls = []
    game.walls.extend(generate_wall(game, [5, 10], [10, 10]))
    game.walls.extend(generate_wall(game, [43, 1], [43, 10]))
