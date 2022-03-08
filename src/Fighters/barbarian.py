from src.Fighters.fighter import Fighter
from src.config import BARBARIAN


class Barbarian(Fighter):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            BARBARIAN["symbol"],
            BARBARIAN["color"],
            startx,
            starty,
            BARBARIAN["damage"],
            BARBARIAN["health"],
            BARBARIAN["move_speed"],
            BARBARIAN["attack_speed"]
        )
