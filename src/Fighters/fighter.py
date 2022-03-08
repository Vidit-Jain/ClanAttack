from src.object import Object
from src.config import *
import time


class Fighter(Object):
    def __init__(self, game, symbol: str, color: str, startx: int, starty: int, damage: int, health: int, move_speed: int, attack_speed: int):
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
        self.attack_speed = attack_speed

    def loop_collide(self, obj_list: list[Object]):
        flag = False
        if obj_list is not None:
            for i in range(0, len(obj_list)):
                flag = flag or self.collide(obj_list[i])
        return flag

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
        if time.monotonic() - self.last_moved < 1 / self.move_speed:
            return

        x, y = self.bound_movement(x, y)
        self.game.screen.remove(self)
        self.x = [self.x[0] + x, self.x[1] + x]
        self.y = [self.y[0] + y, self.y[1] + y]
        flag = False
        flag = flag or self.loop_collide(self.game.huts)
        flag = flag or self.loop_collide(self.game.walls)
        flag = flag or self.loop_collide(self.game.cannons)
        flag = flag or self.loop_collide(self.game.spawnpoints)
        flag = flag or self.collide(self.game.townhall)
        if flag:
            self.x = [self.x[0] - x, self.x[1] - x]
            self.y = [self.y[0] - y, self.y[1] - y]
        self.last_moved = time.monotonic()
