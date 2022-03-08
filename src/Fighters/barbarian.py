from src.Fighters.fighter import Fighter
from src.config import BARBARIAN


class Barbarian(Fighter):
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
            BARBARIAN["attack_speed"]
        )

    def __min_dist(self, obj):
        least_distance = 1e6
        if obj is not None:
            for i in range(obj.x[0], obj.x[1]):
                for j in range(obj.y[0], obj.y[1]):
                    least_distance = min(least_distance, abs(self.x[0] - i) + abs(self.y[0] - j))
        return least_distance

    def __closest_point(self, obj):
        least_distance = 1e6
        x, y = obj.x[0], obj.y[0]
        for i in range(obj.x[0], obj.x[1]):
            for j in range(obj.y[0], obj.y[1]):
                if abs(self.x[0] - i) + abs(self.y[0] - i) < least_distance:
                    x, y = i, j
                    least_distance = abs(self.x[0] - i) + abs(self.y[0] - i)
        return x, y

    def move(self):
        best_hut = None
        for hut in self.game.huts:
            if self.__min_dist(hut) < self.__min_dist(best_hut):
                best_hut = hut
        if best_hut is None:
            return

        x, y = self.__closest_point(best_hut)
        if self.x[0] > x:
            super().move(-1, 0)
        elif self.x[0] < x:
            super().move(1, 0)
        elif self.y[0] > y:
            super().move(0, -1)
        elif self.y[0] < x:
            super().move(0, 1)
