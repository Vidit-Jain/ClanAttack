from src.object import Object
from src.config import *
from src.audio import *
import time


class Fighter(Object):
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
    ):
        super().__init__(
            game,
            symbol,
            color,
            startx,
            starty,
            FIGHTER["height"],
            FIGHTER["width"],
            health,
        )
        self._damage = damage
        self._move_speed = move_speed
        self._last_moved = 0
        self._last_attacked = 0
        self._attack_speed = attack_speed

    def loop_collide(self, obj_list: list[Object]):
        if obj_list is not None:
            for obj in obj_list:
                if self.collide(obj):
                    return obj
        return None

    # Limits movement in case given movement would result in falling off screen
    def bound_movement(self, x: int, y: int):
        if self._x[0] + x < 0:
            x = -self._x[0]
        if self._x[1] + x > self.game.screen.get_width():
            x = self.game.screen.get_width() - self._x[1]

        if self._y[0] + y < 0:
            y = -self._y[0]
        if self._y[1] + y > self.game.screen.get_height():
            y = self.game.screen.get_height() - self._y[1]
        return x, y

    def move(self, x: int, y: int):
        if time.monotonic() - self._last_moved < 1 / (
                self._move_speed * (self.game.rage.get_active() + 1)
        ):
            return

        x, y = self.bound_movement(x, y)
        self._x = [self._x[0] + x, self._x[1] + x]
        self._y = [self._y[0] + y, self._y[1] + y]

        # Return object you collide with and reverts the movement, else None
        obj = self.loop_collide(self.game.huts)
        if obj is None:
            obj = self.loop_collide(self.game.walls)
        if obj is None:
            obj = self.loop_collide(self.game.cannons)
        if obj is None and self.game.townhall is not None:
            obj = self.loop_collide([self.game.townhall])
        if obj is not None:
            self._x = [self._x[0] - x, self._x[1] - x]
            self._y = [self._y[0] - y, self._y[1] - y]
        else:
            self._last_moved = time.monotonic()

        return obj

    def attack(self, obj):
        if time.monotonic() - self._last_attacked < 1 / self._attack_speed:
            return
        self._last_attacked = time.monotonic()
        play("src/AudioFiles/barbarian_attack.mp3")
        obj.damaged(self._damage * (self.game.rage.get_active() + 1))

    def closest_point(self, obj):
        least_distance = 1e6
        x, y = obj.get_x()[0], obj.get_y()[0]
        for i in range(int(obj.get_x()[0]), int(obj.get_x()[1])):
            for j in range(int(obj.get_y()[0]), int(obj.get_y()[1])):
                if abs(self._x[0] - i) + abs(self._y[0] - i) < least_distance:
                    x, y = i, j
                    least_distance = abs(self._x[0] - i) + abs(self._y[0] - i)
        return x, y

    def heal(self):
        self._health = min(
            int(self._health * 1.5), self._max_health
        )
