from src.Fighters.troop import Troop
from src.config import ARCHER


class Archer(Troop):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            ARCHER["symbol"],
            ARCHER["colors"][-1],
            startx,
            starty,
            ARCHER["damage"],
            ARCHER["health"],
            ARCHER["move_speed"],
            ARCHER["attack_speed"],
            ARCHER["sound_file"],
            ARCHER["colors"],
            [game.huts, game.cannons, game.townhall],
        )
        self._range = ARCHER["range"]

    def action(self):
        best = self.best_building()
        if self._Troop__min_dist(best) <= self._range:
            self.attack(best)
        else:
            self.move()
