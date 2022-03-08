from src.object import Object
from src.config import *
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
        self.damage = damage
        self.move_speed = move_speed
        self.last_moved = 0
        self.last_attacked = 0
        self.attack_speed = attack_speed

    def loop_collide(self, obj_list: list[Object]):
        if obj_list is not None:
            for obj in obj_list:
                if self.collide(obj):
                    return obj
        return None

    # Limits movement in case given movement would result in falling off screen
    def bound_movement(self, x: int, y: int):
        if self.x[0] + x < 0:
            x = -self.x[0]
        if self.x[1] + x > GAME["window"]["width"]:
            x = GAME["window"]["width"] - self.x[1]

        if self.y[0] + y < 0:
            y = -self.y[0]
        if self.y[1] + y > GAME["window"]["height"]:
            y = GAME["window"]["height"] - self.y[1]
        return x, y

    def move(self, x: int, y: int):
        if time.monotonic() - self.last_moved < 1 / (self.move_speed * (self.game.rageActive + 1)):
            return

        x, y = self.bound_movement(x, y)
        self.x = [self.x[0] + x, self.x[1] + x]
        self.y = [self.y[0] + y, self.y[1] + y]

        # Return object you collide with and reverts the movement, else None
        obj = self.loop_collide(self.game.huts)
        if obj is None:
            obj = self.loop_collide(self.game.walls)
        if obj is None:
            obj = self.loop_collide(self.game.cannons)
        if obj is None and self.game.townhall is not None:
            obj = self.loop_collide([self.game.townhall])
        if obj is not None:
            self.x = [self.x[0] - x, self.x[1] - x]
            self.y = [self.y[0] - y, self.y[1] - y]
        else:
            self.last_moved = time.monotonic()

        return obj

    def attack(self, obj):
        if time.monotonic() - self.last_attacked < 1 / self.attack_speed:
            return
        self.last_attacked = time.monotonic()
        obj.damaged(self.damage * (self.game.rageActive + 1))

    def closest_point(self, obj):
        least_distance = 1e6
        x, y = obj.x[0], obj.y[0]
        for i in range(int(obj.x[0]), int(obj.x[1])):
            for j in range(int(obj.y[0]), int(obj.y[1])):
                if abs(self.x[0] - i) + abs(self.y[0] - i) < least_distance:
                    x, y = i, j
                    least_distance = abs(self.x[0] - i) + abs(self.y[0] - i)
        return x, y
