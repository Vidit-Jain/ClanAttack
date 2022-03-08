from src.object import Object
from src.config import *
import time


class Fighter(Object):
    def __init__(self, game, symbol, color, startx, starty, damage, health, move_speed, attack_speed):
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

    def bound_movement(self, x: list, y: list):
        if self.x[0] + x < 0:
            x[0] = -self.x[0]
        if self.x[1] + x > GAME["window"]["width"]:
            x[1] = GAME["window"]["width"] - self.x[1]

        if self.y[0] + y < 0:
            y[0] = -self.y[0]
        if self.y[1] + y > GAME["window"]["height"]:
            y[1] = GAME["window"]["height"] - self.y[1]
        return x, y

    def move(self, x: int, y: int):
        if time.monotonic() - self.last_moved < 1 / self.move_speed:
            return

        x, y = self.bound_movement(x, y)
        self.game.screen.remove(self)
        self.x = [self.x[0] + x, self.x[1] + x]
        self.y = [self.y[0] + y, self.y[1] + y]
        self.last_moved = time.monotonic()
