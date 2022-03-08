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
            for i in range(int(obj.x[0]), int(obj.x[1])):
                for j in range(int(obj.y[0]), int(obj.y[1])):
                    least_distance = min(
                        least_distance, abs(self.x[0] - i) + abs(self.y[0] - j)
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
        if self.x[0] > x:
            movement_options.append([-1, 0])
        if self.x[0] < x:
            movement_options.append([1, 0])
        if self.y[0] > y:
            movement_options.append([0, -1])
        if self.y[0] < y:
            movement_options.append([0, 1])
        movement_choice = random.choice(movement_options)

        # collision_obj stores the object you collided with
        collision_obj = super().move(movement_choice[0], movement_choice[1])
        if collision_obj is not None and collision_obj != "spawnpoint":
            self.attack(collision_obj)

    def __update_color(self):
        if self.health / self.max_health >= 0.5:
            self.color = BARBARIAN["colors"][2]
        elif self.health / self.max_health >= 0.2:
            self.color = BARBARIAN["colors"][1]
        else:
            self.color = BARBARIAN["colors"][0]

    def damaged(self, damage: int):
        self.__update_color()
        super().damaged(damage)
