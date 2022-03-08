from src.Fighters.fighter import *


class King(Fighter):
    def __init__(self, game):
        super().__init__(
            game,
            KING["symbol"],
            KING["color"],
            KING["starting_coords"][0],
            KING["starting_coords"][1],
            KING["damage"],
            KING["health"],
            KING["move_speed"],
            KING["attack_speed"],
        )
        self.range = KING["range"]

    def move(self, ch: str):
        if ch == "w":
            super().move(0, -1)
        elif ch == "a":
            super().move(-1, 0)
        elif ch == "s":
            super().move(0, 1)
        else:
            super().move(1, 0)


def add_king(game):
    game.king = King(game)
