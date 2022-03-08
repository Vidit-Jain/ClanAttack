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
    for i in range(
        min(start_wall[0], end_wall[0]), max(start_wall[0], end_wall[0]) + 1
    ):
        for j in range(
            min(start_wall[1], end_wall[1]), max(start_wall[1], end_wall[1]) + 1
        ):
            walls.append(Wall(game, i, j))

    return walls


def add_walls(game):
    game.walls = []
    game.walls.extend(generate_wall(game, [5, 10], [10, 10]))
    game.walls.extend(generate_wall(game, [43, 1], [43, 10]))
    game.walls.extend(generate_wall(game, [56, 11], [56, 27]))
    game.walls.extend(generate_wall(game, [57, 27], [78, 27]))

    game.walls.extend(generate_wall(game, [68, 26], [68, 20]))
    game.walls.extend(generate_wall(game, [69, 20], [75, 20]))
    game.walls.extend(generate_wall(game, [76, 26], [76, 20]))

    game.walls.extend(generate_wall(game, [79, 27], [79, 31]))
    game.walls.extend(generate_wall(game, [80, 31], [95, 31]))
    game.walls.extend(generate_wall(game, [80, 31], [95, 31]))
    game.walls.extend(generate_wall(game, [95, 30], [95, 27]))
    game.walls.extend(generate_wall(game, [94, 27], [90, 27]))
    game.walls.extend(generate_wall(game, [90, 26], [90, 25]))
    game.walls.extend(generate_wall(game, [91, 25], [96, 25]))
    game.walls.extend(generate_wall(game, [96, 24], [96, 11]))
    game.walls.extend(generate_wall(game, [95, 11], [57, 11]))
