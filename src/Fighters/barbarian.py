from src.Fighters.fighter import Fighter
from src.config import BARBARIAN
import random


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
            BARBARIAN["attack_speed"],
        )

    def __min_dist(self, obj):
        least_distance = 1e6
        if obj is not None:
            for i in range(int(obj.get_x()[0]), int(obj.get_x()[1])):
                for j in range(int(obj.get_y()[0]), int(obj.get_y()[1])):
                    least_distance = min(
                        least_distance, abs(self._x[0] - i) + abs(self._y[0] - j)
                    )
        return least_distance

    def best_building(self):
        best = None

        for hut in self.game.huts:
            if self.__min_dist(hut) < self.__min_dist(best):
                best = hut

        for cannon in self.game.cannons:
            if self.__min_dist(cannon) < self.__min_dist(best):
                best = cannon

        if self.game.townhall is not None and self.__min_dist(
            self.game.townhall
        ) < self.__min_dist(best):
            best = self.game.townhall

        return best

    def move(self):

        # Closest building for barbarian to go to
        best = self.best_building()
        if best is None:
            return

        x, y = self.closest_point(best)
        movement_options = []
        if self._x[0] > x:
            movement_options.append([-1, 0])
        if self._x[0] < x:
            movement_options.append([1, 0])
        if self._y[0] > y:
            movement_options.append([0, -1])
        if self._y[0] < y:
            movement_options.append([0, 1])

        if len(movement_options) == 2:
            a = [movement_options[0][0] + movement_options[1][0],
                 movement_options[0][1] + movement_options[1][1]]
            try_diagonal = super().move(a[0], a[1])
            # If no error then you're done
            if try_diagonal is None:
                return

        movement_choice = random.choice(movement_options)

        # collision_obj stores the object you collided with
        collision_obj = super().move(movement_choice[0], movement_choice[1])
        if collision_obj is not None:
            self.attack(collision_obj)

    def __update_color(self):
        if self._health / self._max_health >= 0.5:
            self._color = BARBARIAN["colors"][2]
        elif self._health / self._max_health >= 0.2:
            self._color = BARBARIAN["colors"][1]
        else:
            self._color = BARBARIAN["colors"][0]

    def damaged(self, damage: int):
        self.__update_color()
        super().damaged(damage)
