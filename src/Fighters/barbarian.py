from src.Fighters.troop import Troop
from src.config import BARBARIAN


class Barbarian(Troop):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            BARBARIAN["symbol"],
            BARBARIAN["colors"][-1],
            startx,
            starty,
            BARBARIAN["damage"],
            BARBARIAN["health"],
            BARBARIAN["move_speed"],
            BARBARIAN["attack_speed"],
            BARBARIAN["sound_file"],
            BARBARIAN["colors"],
            [game.huts, game.cannons, game.townhall],
        )

    def action(self):
        self.move()
