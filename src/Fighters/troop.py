from src.Fighters.fighter import *
import random

class Troop(Fighter):
    def __init__(
            self,
            game,
            symbol: str,
            color: str,
            startx: int,
            starty: int,
            damage: int,
            health: int,
            move_speed: int,
            attack_speed: int,
            sound_file: str,
            colors: list,
            building_preferences: list,
            collision_buildings: list = None
    ):
        super().__init__(
            game,
            symbol,
            color,
            startx,
            starty,
            damage,
            health,
            move_speed,
            attack_speed,
            sound_file,
            collision_buildings
        )
        self._colors = colors
        self._building_preferences = building_preferences

    def __update_color(self):
        if self._health / self._max_health >= 0.5:
            self._color = self._colors[2]
        elif self._health / self._max_health >= 0.2:
            self._color = self._colors[1]
        else:
            self._color = self._colors[0]

    def damaged(self, damage: int):
        self.__update_color()
        super().damaged(damage)

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

        for i in range(len(self._building_preferences)):
            for building in self._building_preferences[i]:
                if self.__min_dist(building) < self.__min_dist(best):
                    best = building
        return best

    def move(self):

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

        # If you're supposed to be on top
        if len(movement_options) == 0:
            return

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

    def attack(self, obj):
        if not super().attack():
            return
        obj.damaged(self._damage * (self.game.rage.get_active() + 1))
