from src.Fighters.troop import Troop
from src.config import BALLOON


class Balloon(Troop):
    def __init__(self, game, startx: int, starty: int):
        super().__init__(
            game,
            BALLOON["symbol"],
            BALLOON["colors"][-1],
            startx,
            starty,
            BALLOON["damage"],
            BALLOON["health"],
            BALLOON["move_speed"],
            BALLOON["attack_speed"],
            BALLOON["colors"],
            [game.wizards, game.cannons, game.townhall, game.huts],
            []
        )

    def best_building(self):
        best = None
        for i in range(2):
            for building in self._building_preferences[i]:
                if self._Troop__min_dist(building) < self._Troop__min_dist(best):
                    best = building
        if best is not None:
            return best
        return super().best_building()

    def action(self):
        self.move()
        best = self.best_building()
        if self._Troop__min_dist(best) == 0:
            self.attack(best)
